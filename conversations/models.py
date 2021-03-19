from django.db import models
from django.contrib.auth.models import auth, User


class Conversation(models.Model):
    name = models.CharField(max_length=64)
    logo = models.URLField()
    description = models.TextField(max_length=75)
    participants = models.ManyToManyField(User)
    url_id = models.CharField(max_length=15)
    is_link = models.BooleanField(default=False)
    is_permission = models.BooleanField(default=False)