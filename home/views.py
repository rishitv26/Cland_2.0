from django.shortcuts import render
from conversations.models import *

def index(request):
    con = Conversation.objects.all()
    return render(request, "home.html", {
        'cons': con
    })