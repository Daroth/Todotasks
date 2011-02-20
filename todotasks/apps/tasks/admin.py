from django.contrib.admin.options import ModelAdmin
from django.contrib.admin import site
from apps.tasks.models import Task

class TaskAdmin(ModelAdmin):
    list_display = ('id', 'title', 'created', 'modified', 'created_by', 'is_finished',)
    list_display_links = ('id', 'title',)
    list_filter = ('created', 'modified', 'is_finished',)
    search_fields = ['title', 'description',]

site.register(Task, TaskAdmin)