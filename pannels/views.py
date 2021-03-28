from django.shortcuts import render


def adminPage(request):
    if request.user.username == 'rishit':
        return render(request, 'admin-pannel.html')
    else:
        return render(request, '404.html')

def emailPage(request):
    return render(request, 'email.html')