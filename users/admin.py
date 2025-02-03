from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "image")  # Show username and profile picture in admin panel
    search_fields = ("user__username",)  # Allow searching by username
    list_filter = ("user",)
