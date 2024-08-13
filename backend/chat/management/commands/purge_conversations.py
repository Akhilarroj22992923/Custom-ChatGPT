from django.core.management.base import BaseCommand
from chat.models import Conversation
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Purge old conversation records'

    def handle(self, *args, **kwargs):
        retention_period = 60  # Days to keep the conversation records
        cutoff_date = timezone.now() - timedelta(days=retention_period)
        old_conversations = Conversation.objects.filter(created_at__lt=cutoff_date)
        count, _ = old_conversations.delete()
        self.stdout.write(self.style.SUCCESS(f'{count} old conversation(s) purged successfully'))
