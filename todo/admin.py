from django.contrib import admin
from .models import Todo, SiteConfig

admin.site.site_header = "ToDo App"
admin.site.site_title = "ToDo Admin Panel"
admin.site.index_title = "Welcome to ToDo Admin"

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "completed", "created_at", "modified_at")
    list_filter = ("completed", "user")
    search_fields = ("title", "user__username")

@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('auto_delete_days',)
