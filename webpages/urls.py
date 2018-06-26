from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('events/', views.events_page),
    path('events/hackathon/', views.events_hackathon_page),
    path('register/', views.register_page),
    path('login/', views.login_page)
]