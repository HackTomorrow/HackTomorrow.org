from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request, ):
    return redirect(hackathon_page)

def hackathon_page(request, ):
    return render(request, "pages/hackathon.html", context=None)

def register_page(request, ):
    return render(request, "pages/register.html", context=None)
