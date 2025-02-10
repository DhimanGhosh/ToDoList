from django.core.management.base import BaseCommand
from django.utils.timezone import now
from todo.models import Todo, SiteConfig
from datetime import timedelta

class Command(BaseCommand):
    help = "Delete completed tasks older than a certain number of days"

    def handle(self, *args, **kwargs):
        config = SiteConfig.objects.first()  # Get the auto-delete config
        if config:
            auto_delete_days = config.auto_delete_days
            cutoff_date = now() - timedelta(days=auto_delete_days)
            old_completed_tasks = Todo.objects.filter(completed=True, modified_at__lt=cutoff_date)
            
            count = old_completed_tasks.count()
            old_completed_tasks.delete()
            
            self.stdout.write(self.style.SUCCESS(f"{count} old completed tasks deleted."))
        else:
            self.stdout.write(self.style.WARNING("No auto-delete configuration found."))
