from __future__ import print_function
from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
import json
from django.views import View

class IndexView(View):

    def get(self, request) -> HttpResponse:
        return redirect("hackathon_page")

class EventsView(View):

    def get(self, request) -> HttpResponse:
        return redirect("hackathon_page")

class HackathonView(View):
    
    def get(self, request) -> HttpResponse:
        return render(request, "pages/hackathon.html", context=None)

class RegisterView(View):

    def get(self, request) -> HttpResponse:
        return render(request, "pages/register.html", context=None)

    def post(self, request) -> HttpResponse:
        form = request.POST
        error = 
        if form["password"] == form["password_again"]:
            try:
                #promise = auth.create_user_with_email_and_password(form["email"],form["password"])
            except Exception as e:
                print(e)
                error = "critical"
        else:
            error = "passwords_dont_match"
        return render(request, "pages/register.html", {"error":error})

class Loginiew(View):

    def get(self, request) -> HttpResponse:
        return render(request, "pages/login.html", context=None)
    
    def post(self, request) -> HttpResponse:
        pass