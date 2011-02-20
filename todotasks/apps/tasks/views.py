# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from apps.tasks.forms import TaskForm
from apps.tasks.models import Task

@login_required
def create_tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return HttpResponseRedirect(reverse('read-project', args=(task.project.id,)))
    else:
        form = TaskForm()
    params = {'form':form, 'user': request.user }
    params.update(csrf(request))
    return render_to_response('tasks/task_form.html', params)

@login_required
def mark_as_done(request, object_id):
    task = get_object_or_404(Task, id=object_id)
    if not task.is_finished:
        task.is_finished = True
        task.save()
    return HttpResponseRedirect(reverse('read-project', args=(task.project.id,)))