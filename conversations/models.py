from django.db import models
from django.contrib.auth.models import auth, User


class Conversation(models.Model):
    name = models.CharField(max_length=64)
    logo = models.URLField()
    description = models.TextField(max_length=1863)
    participants = models.ManyToManyField(User)
    url_id = models.CharField(max_length=15)