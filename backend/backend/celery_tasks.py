from celery import shared_task
from django.core.management import call_command

@shared_task
def purge_old_conversations():
    call_command('purge_conversations')
