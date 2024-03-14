from django.http.response import HttpResponse

from django.shortcuts import render

# Create your views here.e
def django(request):
    return HttpResponse('Welcome django')
