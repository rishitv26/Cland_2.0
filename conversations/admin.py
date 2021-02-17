from django.contrib import admin
from .models import Conversations

class ConversationsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'admin',
        'description',
    ]

admin.site.register(Conversations, ConversationsAdmin)