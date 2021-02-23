from django.contrib import admin
from .models import Conversations


class ConversationsAdmin(admin.ModelAdmin):
    list_display = ['title', 'admin', 'image_url', 'description']

admin.site.register(Conversations, ConversationsAdmin)