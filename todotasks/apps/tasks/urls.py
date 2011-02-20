from django.conf.urls.defaults import *
from apps.tasks.forms import TaskForm
from apps.tasks.models import Task

urlpatterns = patterns('',
                       url(r'^$', 'django.views.generic.list_detail.object_list',
                           {'queryset':Task.objects.all().order_by('-created'),}, name='list-tasks'),
                       url(r'^create/$', 'apps.tasks.views.create_tasks', {}, name='create-task'),
                       url(r'^task/(?P<object_id>\d+)$', 'django.views.generic.list_detail.object_detail',
                           {'queryset':Task.objects.all(),},name='read-task'),
                       url(r'^task/delete/(?P<object_id>\d+)$', 'django.views.generic.create_update.delete_object',
                           {'model':Task,'post_delete_redirect':'/', 'login_required':True}, name='delete-task'),
                       (r'^task/done/(?P<object_id>\d+)$', 'apps.tasks.views.mark_as_done'),
                       )
