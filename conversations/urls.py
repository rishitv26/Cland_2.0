from django.urls import path
from . import views

urlpatterns = [
    path('<str:con>/', views.chat, name='user conversations'),
]