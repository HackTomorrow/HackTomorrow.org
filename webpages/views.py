from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
import json

def index(request, ) -> HttpResponse:
    return redirect(events_hackathon_page)

def events_page(request, ) -> HttpResponse:
    return redirect(events_hackathon_page)

def events_hackathon_page(request, ) -> HttpResponse:
    return render(request, "pages/hackathon.html", context=None)

def register_page(request, ) -> HttpResponse: 
    return render(request, "pages/register.html", context=None)

def login_page(request, ) -> HttpResponse:
    return render(request, "pages/login.html", context=None)