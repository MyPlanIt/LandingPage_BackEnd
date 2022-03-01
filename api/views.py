from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(self):
    return HttpResponse({"hello"})