from django.shortcuts import render
from django.http import HttpResponse

#C:\Users\Sakib Chowdhury\django_practice\Step-03\my_project\templates
def index(request):
    return render(request,'index.html')