from django.shortcuts import render
from django.http import HttpResponse


def index(request): #takes in a request and returns a response
    return HttpResponse("Hello, world. You're at the movies index.") #returns a simple response with a string

# Create your views here.
