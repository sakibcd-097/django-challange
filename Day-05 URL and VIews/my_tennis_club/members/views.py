from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def name(request):
    return HttpResponse('Hello!')

def cake(request):
    return HttpResponse('This is my cake')