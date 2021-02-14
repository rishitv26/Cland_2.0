from django.db import models


class Conversation(models.Model):
    title = models.CharField(max_length=64)
    pic = models.CharField(max_length=2000)
    bg_pic = models.CharField(max_length=2000)