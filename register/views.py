from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Email = request.POST['email']
        FullName = request.POST['name']
        Password = request.POST['passwordD']
        Passwordcon = request.POST['passwordC']

        if Password == Passwordcon:
            if User.objects.filter(username=Username).exists():
                messages.info(request, "Username is already used.")
                return render(request, 'register.html')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "Email is already used.")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=Username, password=Passwordcon, email=Email, first_name=FullName, last_name='no data')
                user.save()
                return redirect("/")
        else:
            messages.info(request, "Confirm your password, please.")
            return render(request, 'register.html')
    else: 
        return render(request, 'register.html')