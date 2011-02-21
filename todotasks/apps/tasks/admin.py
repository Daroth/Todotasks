from django.contrib.admin.options import ModelAdmin
from django.contrib.admin import site
from apps.tasks.models import Task, Project

class TaskAdmin(ModelAdmin):
    list_display = ('id', 'title', 'title_slug', 'created', 'modified', 'created_by', 'is_finished', 'project')
    list_display_links = ('id', 'title',)
    list_filter = ('created', 'modified', 'is_finished',)
    search_fields = ['title', 'description',]

class ProjectAdmin(ModelAdmin):
    list_display = ('id', 'title', 'title_slug', 'created', 'modified',)
    list_display_links = ('id', 'title',)
    list_filter = ('created', 'modified',)
    search_fields = ['title', 'description',]

site.register(Task, TaskAdmin)
site.register(Project, ProjectAdmin)