from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request, ):
    return redirect(events_hackathon_page)

def events_page(request, ):
    return rediret(events_hackathon_page):

def events_hackathon_page(request, ):
    return render(request, "pages/hackathon.html", context=None)

def register_page(request, ):
    return render(request, "pages/register.html", context=None)
