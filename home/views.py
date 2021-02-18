from django.shortcuts import render
from conversations.models import Conversations

def index(request):
    con = Conversations.objects.all()
    return render(request, "home.html", {
        'cons': con
    })