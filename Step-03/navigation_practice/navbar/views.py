from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    d={'name':'Rahim', 'age':25, 'courses':[
        {
            'id':1,
            'name':'Sakib',
            'roll':25
        },
        {
            'id':2,
            'name':'Rahim',
            'roll':24
            
        }
        ]}
    return render(request,"navbar/about.html",d)
def contact(request):
    return render(request,"navbar/contact.html")