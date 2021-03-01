from django.db import models


class Conversations(models.Model):
    title = models.CharField(max_length=64)
    admin = models.CharField(max_length=74)
    image_url = models.CharField(max_length=2000)
    description = models.CharField(max_length=1074)


class Corporation(models.Model):
    name = models.CharField(max_length=64)
    admins = 'not availible as per now...'
    logo = models.URLField()
    description = models.TextField(max_length=1863)
    co_admin = 'not availible as per now...'
    staff_workers = 'not availible as per now...'
    url_id = models.CharField(max_length=15)