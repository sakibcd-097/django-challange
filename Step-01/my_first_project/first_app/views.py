from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello!</h1> <a href='contact/'>Contact</a> <a href='about/'>About</a>")


def contact(request):
    return HttpResponse("<h1>This is contact page</h1>")

def about(request):
    return HttpResponse("<h1>This is about page</h1>")


