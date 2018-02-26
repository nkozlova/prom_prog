from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class ModelWithDates(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(ModelWithDates):
    title = models.CharField(max_length=255, default='')
    description = models.TextField()
    mark_as_done = models.BooleanField(default=False)
