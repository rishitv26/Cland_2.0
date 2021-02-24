from django.shortcuts import render

def create_chat(request):
    return render(request, 'create-chat.html')