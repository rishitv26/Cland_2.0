from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, auth

def create_chat(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        logo = request.POST['logo']
        is_link = request.POST['is_link']
        is_permission = request.POST['is_permission']
    
    else:
        return render(request, 'create-chat.html')

def conversation(request, id):
    
    all_ids = None
    all_ids = Conversation.objects.get(
        url_id=id
    )


    return render(request, 'conversation.html', {
        'ids': all_ids
    })