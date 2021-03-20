from django.db import models
from django.contrib.auth.models import auth, User


class Conversation(models.Model):
    name = models.CharField(max_length=64)
    logo = models.URLField()
    description = models.TextField(max_length=75)
    participants = models.ManyToManyField(User)
    url_id = models.CharField(max_length=15)


class Conversation_permissions(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    is_link = models.BooleanField(default=False)
    is_particapant_permission = models.BooleanField(default=False)