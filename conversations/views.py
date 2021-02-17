from django.shortcuts import render

def chat(request, con):
    name = con
    return render(request, 'conversations-per-user.html', {
        'name': name
    })