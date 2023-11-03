import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from DJSapp.models import SchedulerInterval

logger = logging.getLogger(__name__)

def my_job():
    try:
        # Get the SchedulerInterval from the database
        interval = SchedulerInterval.objects.get(pk=1)  # You can adjust the logic to fetch the desired interval
        interval_seconds = interval.interval
    except SchedulerInterval.DoesNotExist:
        # Use a default interval if the record doesn't exist
        interval_seconds = 10  # Default to 10 seconds
    print('nasvai')
    # Your job processing logic here, using interval_seconds...

def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        def schedule_my_job(scheduler):
            try:
                # Get the SchedulerInterval from the database
                interval = SchedulerInterval.objects.get(pk=1)  # You can adjust the logic to fetch the desired interval
                interval_seconds = interval.interval
            except SchedulerInterval.DoesNotExist:
                # Use a default interval if the record doesn't exist
                interval_seconds = 10  # Default to 10 seconds

            trigger = IntervalTrigger(seconds=interval_seconds)
            scheduler.add_job(
                my_job,
                trigger=trigger,
                id="my_job",
                max_instances=1,
                replace_existing=True,
            )
            logger.info(f"Added job 'my_job' with an interval of {interval_seconds} seconds.")

        schedule_my_job(scheduler)

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
