from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def member(request):
    return HttpResponse('Hello Sakib!')

def add(request):
    a=23+2
    
    return HttpResponse(a)


