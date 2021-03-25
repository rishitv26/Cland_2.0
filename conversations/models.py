from django.db import models
from django.contrib.auth.models import auth, User


'''class Conversation(models.Model):
    name = models.CharField(max_length=64)
    logo = models.URLField()
    description = models.TextField(max_length=75)
    url_id = models.CharField(max_length=15)

class Conversation_participants(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)'''
