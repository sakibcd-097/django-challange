from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def table(request):
    return HttpResponse('This my table!')
