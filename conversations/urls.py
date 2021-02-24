from django.urls import path
from . import views

urlpatterns = [
    path('create-conversation/', views.create_chat, name='create conversations'),
]