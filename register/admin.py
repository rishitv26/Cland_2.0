from django.contrib import admin
from .models import *


class User_picAdmin(admin.ModelAdmin):
    list_display = ['user', 'pic']

admin.site.register(User_pic, User_picAdmin)