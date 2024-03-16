from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def mem(request):
    return HttpResponse('Welcoome django')


def bkash(request):
    return HttpResponse('Payment by using bkash')