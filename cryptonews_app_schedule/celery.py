from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Укажите имя вашего проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptonews_app_schedule.settings')

app = Celery('cryptonews_app_schedule')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
