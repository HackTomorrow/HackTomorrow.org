from __future__ import print_function
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render
import requests
import json

class IndexView(View):

    def get(self, request) -> HttpResponse:
        return redirect("hackathon_page")

class EventsView(View):

    def get(self, request) -> HttpResponse:
        return redirect("hackathon_page")

class NineteenView(View):

    def get(self, request) -> HttpResponse:
        return redirect("hackathon_page")

class HackathonView(View):
    
    def get(self, request) -> HttpResponse:
        return render(request, "pages/hackathon.html", context=None)

class RegisterView(View):

    def get(self, request) -> HttpResponse:
        return render(request, "pages/register.html", context=None)

    def post(self, request) -> HttpResponse:
        return HttpResponse("hello")

class Loginiew(View):

    def get(self, request) -> HttpResponse:
        return render(request, "pages/login.html", context=None)
    
    def post(self, request) -> HttpResponse:
        pass