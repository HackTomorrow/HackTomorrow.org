from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
import json

def index(request, ):
    return redirect(events_hackathon_page)

def events_page(request, ):
    return redirect(events_hackathon_page)

def events_hackathon_page(request, ):
    return render(request, "pages/hackathon.html", context=None)

def events_dashboard_page(request, ):
    header = {}
    events = requests.get("api.hacktomorrow.org/events", header=header)
    return render(request, "pages/dashboard.html", {"events" : json.loads(events)})

def register_page(request, ):
    return render(request, "pages/register.html", context=None)