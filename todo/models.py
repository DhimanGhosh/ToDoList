from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Ensure it's nullable at first
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username if self.user else 'No User'}"

    class Meta:
        ordering = ['completed']

class SiteConfig(models.Model):
    auto_delete_days = models.PositiveIntegerField(default=7)  # Default to 7 days

    def __str__(self):
        return f"Auto-delete tasks after {self.auto_delete_days} days"
