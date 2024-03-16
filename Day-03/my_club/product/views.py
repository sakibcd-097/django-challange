from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cake(request):
    return HttpResponse('This is my cake!')