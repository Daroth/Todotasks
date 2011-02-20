from django.forms.models import ModelForm
from apps.tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('created_by', 'is_finished',)