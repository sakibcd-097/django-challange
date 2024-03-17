from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def django(request):
    return HttpResponse('Hello! Sakib Chowdhury')


def add(reuqest):
    a=34+2
    return HttpResponse(a)