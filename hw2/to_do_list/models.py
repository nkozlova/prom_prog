from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)


class ModelWithDates(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    finished = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(ModelWithDates):
    title = models.CharField(max_length=255, default='')
    description = models.TextField()
    mark_as_done = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.title
