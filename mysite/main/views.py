from django.shortcuts import render
from django.http import HttpReponse

# Create your views here.
def index(response):
    return HttpReponse("Tech with Tim")