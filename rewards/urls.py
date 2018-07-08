from django.urls import path
from . import views

urlpatterns = [
    path("rewards/"),
    path("rewards/challenges/"),
    path("rewards/prizes"),
    path("rewards/challenges/complete"),
]