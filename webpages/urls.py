from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('events/', views.EventsView.as_view(), name="events_page"),
    path('events/hackathon/', views.HackathonView.as_view(), name="hackathon_page"),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.Loginiew.as_view()),
]