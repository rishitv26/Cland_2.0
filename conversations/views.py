from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, auth
import random

def create_chat(request):
    all_users = User.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        logo = request.POST['logo']
        participant = request.POST['participant']

        part_names = participant.split()
        print(part_names)

        # selected_user = User.objects.filter(
        #     first_name = part_names[1],
        #     last_name = part_names[2]
        # )

        # url_id = round(random.randrange(100000000000000, 999999999999999))

        # conversation = Conversation(name=name, logo=logo, description=description, participants=selected_user, url_id=url_id)
        # conversation.save()

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