from django.contrib import admin
from home.models import UserPics

class UserpicsAdmin(admin.ModelAdmin):
    list_display = ['pic', 'user']

admin.site.register(UserPics, UserpicsAdmin)