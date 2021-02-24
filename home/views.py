from django.shortcuts import render
from corporations.models import *

def index(request):
    con = Corporation.objects.all()
    return render(request, "home.html", {
        'cons': con
    })