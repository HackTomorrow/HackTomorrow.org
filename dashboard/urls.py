from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="dashboard")
    path("dashboard/events", views.EventsView.as_view(), name="events_dashboard")
]