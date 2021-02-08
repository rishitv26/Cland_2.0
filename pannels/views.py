from django.shortcuts import render


def adminPage(request):
    return render(request, 'admin-pannel.html')