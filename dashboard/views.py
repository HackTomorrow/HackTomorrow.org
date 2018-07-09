from django.shortcuts import render, redirect
from django.http import HttpResponse
import firebase_admin
from django.views import View
from firebase_admin import credentials
from firebase_admin import auth

#cred = credentials.Certificate('path/to/serviceAccountKey.json')
#default_app = firebase_admin.initialize_app(cred)

class DashboardView(View):
    
    def get(self, request) -> HttpResponse:
        return redirect("events_dashboard")

class EventsView(View):

    def get(self, request) -> HttpResponse:
        pass
