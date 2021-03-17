from django.shortcuts import render
from .models import *

def create_chat(request):
    return render(request, 'create-chat.html')

def corporation(request, id):
    
    all_ids = None
    all_ids = Conversation.objects.get(
        url_id=id
    )


    return render(request, 'conversation.html', {
        'ids': all_ids
    })