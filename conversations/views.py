from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.models import User, auth
import random

def create_chat(request):
    all_users = User.objects.all().exclude(username=request.user.username)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        logo = request.POST['logo']
        participant = request.POST['participant']

        selected_user = get_object_or_404(
            User, username = participant
        )

        url_id = round(random.randrange(100000000000000, 999999999999999))

        conversation = Conversation(name=name, logo=logo, description=description, url_id=url_id,)
        participants = Conversation_participants(conversation=conversation, participant=selected_user)
        conversation.save()
        participants.save()

        return render(request, 'create-chat.html', {
            'users': all_users
        })

    else:
        return render(request, 'create-chat.html', {
            'users': all_users
        })

def conversation(request, id):
    
    all_ids = None
    all_ids = Conversation.objects.get(
        url_id=id
    )


    return render(request, 'conversation.html', {
        'ids': all_ids
    })