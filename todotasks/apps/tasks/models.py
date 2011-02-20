from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

# Create your models here.

class Project(TimeStampedModel):
    title = models.CharField(max_length=42)
    description = models.TextField()
    

class Task(TimeStampedModel):
  title = models.CharField(max_length=42)
  description = models.TextField()
  created_by = models.ForeignKey(User)
  is_finished = models.BooleanField(default=False)
  project = models.ForeignKey(Project)

  def __unicode__(self):
    return self.title

  @models.permalink
  def get_absolute_url(self):
    return ('read-task', (), {'object_id':self.id,})