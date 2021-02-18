from django.shortcuts import render

def index(request):
    cons = Conversations.objects.all()

    return render(request, "home.html", {
        'cons': cons
    })