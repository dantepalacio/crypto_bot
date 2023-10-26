from django.db import models

class SchedulerInterval(models.Model):
    interval = models.PositiveIntegerField(verbose_name='Interval (seconds)')

    def __str__(self):
        return f'{self.interval} seconds'
