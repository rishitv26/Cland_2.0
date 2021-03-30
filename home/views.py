from django.shortcuts import render
from conversations.models import *
from register.models import *
from django.contrib.auth.models import User

def index(request):
    profile_pic = None
    con = Conversation.objects.all()
    if request.user.username != '':
        current_user = User.objects.get(username=request.user.username)
        profile_pic = User_pic.objects.get(user=current_user)

    return render(request, "home.html", {
        'cons': con,
        'pic': profile_pic
    })