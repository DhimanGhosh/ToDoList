from django.contrib import admin
from .models import Todo, Profile

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "completed", "created_at", "modified_at")
    list_filter = ("completed", "user")
    search_fields = ("title", "user__username")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "image")  # Show username and profile picture in admin panel
    search_fields = ("user__username",)  # Allow searching by username
    list_filter = ("user",)
