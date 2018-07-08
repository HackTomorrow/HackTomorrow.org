from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
import jwt
import requests
import boto3

class ChallengeView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass

class PrizeView(View):
    
    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass

class CompleteChallengeView(View):
    
    def post(self, request):
        pass