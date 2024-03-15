from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def django(request):
    return HttpResponse('Welcoome django')