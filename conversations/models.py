from django.db import models


class Conversations(models.Model):
    title = models.CharField(max_length=64)
    admin = models.CharField(max_length=74)
    image_url = models.CharField(max_length=2000)
    description = models.CharField(max_length=1074)