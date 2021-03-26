from django.contrib import admin
from .models import *


class ConversationAdmin(admin.ModelAdmin):
    list_display = ['name', 'url_id', 'description']

class Conversation_participantsAdmin(admin.ModelAdmin):
    list_display = ['participant', 'conversation']


admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Conversation_participants, Conversation_participantsAdmin)