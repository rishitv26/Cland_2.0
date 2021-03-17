from django.contrib import admin
from .models import *


class ConversationAdmin(admin.ModelAdmin):
    list_display = ['name', 'url_id', 'description']


admin.site.register(Conversation, ConversationAdmin)