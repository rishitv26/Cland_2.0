from django.shortcuts import render

def chat(request, con):
    name = con
    return render(request, 'chat.html', {
        'name': name
    })