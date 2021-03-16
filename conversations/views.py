from django.shortcuts import render
from .models import *

def create_chat(request):
    return render(request, 'create-chat.html')

def corporation(request, id):
    
    all_ids = Corporation.objects.get(
        url_id=id
    )


    return render(request, 'corporation.html', {
        'corporation': id,
        'ids': all_ids
    })