from django.contrib import admin
from .models import *


class ConversationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'admin', 'image_url', 'description']

class CorporationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'url_id']

admin.site.register(Conversations, ConversationsAdmin)
admin.site.register(Corporation, CorporationAdmin)