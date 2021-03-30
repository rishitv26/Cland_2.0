from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import *


def register(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Email = request.POST['email']
        FullName = request.POST['name']
        LastName = request.POST['last_name']
        Password = request.POST['passwordD']
        Passwordcon = request.POST['passwordC']
        Pic = request.POST['pic']

        if Password == Passwordcon:
            if User.objects.filter(username=Username).exists():
                messages.info(request, "Username is already used.")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=Username, password=Passwordcon, email=Email, first_name=FullName, last_name=LastName)
                if Pic == '':
                    Pic = 'https://eecs.ceas.uc.edu/DDEL/images/default_display_picture.png/@@images/image.png'
                user_pic = User_pic(user=user, pic=Pic)
                user.save()
                user_pic.save()
                return redirect("/")
        else:
            messages.info(request, "Confirm your password, please.")
            return render(request, 'register.html')
    else: 
        return render(request, 'register.html')