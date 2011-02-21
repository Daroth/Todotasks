from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField, AutoSlugField
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class Project(TimeStampedModel):
    """
    A project contains a list of tasks to achieve.
    """
    title = models.CharField(max_length=42)
    title_slug = AutoSlugField(populate_from='title')
    description = models.TextField()

    def __unicode__(self):
        return self.title


class Task(TimeStampedModel):
    """
    A task is a sub part of a project.
    """
    title = models.CharField(max_length=42)
    title_slug = AutoSlugField(populate_from='title')
    description = models.TextField()
    created_by = models.ForeignKey(User)
    is_finished = models.BooleanField(default=False)
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('read-task', (), {'slug':self.title_slug,})