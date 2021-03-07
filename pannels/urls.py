from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.adminPage, name="advanced administration"),
    path('mail/', views.emailPage, name='email'),
]