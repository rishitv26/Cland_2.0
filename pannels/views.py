from django.shortcuts import render


def adminPage(request):
    return render(request, 'admin-pannel.html')

def emailPage(request):
    return render(request, 'email.html')