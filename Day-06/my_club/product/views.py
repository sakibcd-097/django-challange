from django.shortcuts import render


# Create your views here.

def cake(request):
    return render(request,'product.html')
