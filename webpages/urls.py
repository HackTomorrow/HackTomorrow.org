from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hackathon/', views.hackathon_page),
    path('register/', views.register_page),
]