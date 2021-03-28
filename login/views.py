from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if request.user.username == 'rishit':
                return redirect('http://127.0.0.1:8000/pannels/admin/')
            else:
                return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')