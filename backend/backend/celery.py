from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('FULLSTACK-ASSIGNMENT')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(): #debugging that prints information about the current request.
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'purge-old-conversations': {
        'task': 'backend.celery_tasks.purge_old_conversations',
        'schedule': crontab(hour=0, minute=0),  # daily at midnight
    },
}