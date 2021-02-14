from django.shortcuts import render
from .models import UserPics

def index(request):
    pics = UserPics.objects.all()
    return render(request, "home.html", {
       'pics': pic 
    })