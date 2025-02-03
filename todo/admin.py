from django.contrib import admin
from .models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "completed", "created_at", "modified_at")
    list_filter = ("completed", "user")
    search_fields = ("title", "user__username")
