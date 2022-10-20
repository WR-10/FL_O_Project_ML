from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
class Users(AbstractUser):
    profile = models.TextField(max_length=500, blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'followed')
    # nickname = models.CharField(max_length=20, blank=True)
