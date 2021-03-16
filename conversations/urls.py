from django.urls import path
from . import views

urlpatterns = [
    path('create-corporation/', views.create_chat, name='create conversations'),
    path('<int:id>/', views.corporation),
]