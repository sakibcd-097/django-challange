from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def door(request):
    return HttpResponse('This my door!')