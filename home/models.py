from django.db import models


class UserPics(models.Model):
    pic = models.ImageField(upload_to='pics')
    user = models.CharField(max_length=64)