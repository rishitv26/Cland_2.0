from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.models import User, auth
import random
from django.core.mail import send_mail

def create_chat(request):
    all_users = User.objects.all().exclude(username=request.user.username)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        logo = request.POST['logo']
        participant = request.POST['participant']

        if description == '':
            description = 'No Description'

        selected_user = User.objects.get(
            username=participant
        )

        url_id = round(random.randrange(100000000000000, 999999999999999))

        all_ids = None
        def check():
            all_ids = Conversation.objects.filter(
                url_id=url_id
            )
        
        check()
        while all_ids != None:
            round(random.randrange(100000000000000, 999999999999999))
            check()

        conversation = Conversation(name=name, logo=logo, description=description, url_id=url_id,)
        participants = Conversation_participants(conversation=conversation, participant=selected_user)
        conversation.save()
        participants.save()
        
        return redirect('/')

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