from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def name(request):
    return HttpResponse('Hello!')

def cake(request):
    return HttpResponse('This is my cake')





def emoji_converter(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        converted_text = ""
        for char in text:
            if char.isalpha():
                converted_text += chr(ord(char) + 128512)  # Convert to emoji code point
            else:
                converted_text += char
        return render(request, 'emoji_converter.html', {'converted_text': converted_text})
    return render(request, 'emoji_converter.html')




def random_joke(request):
    response = requests.get('https://api.jokes.com/random')  # Example API endpoint
    if response.status_code == 200:
        joke = response.json().get('joke')
        return render(request, 'random_joke.html', {'joke': joke})
    return render(request, 'random_joke.html', {'joke': 'Failed to retrieve joke'})


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})



def my_view(request):
    my_objects = MyModel.objects.all()
    return render(request, 'my_template.html', {'objects': my_objects})


from .models import MyModel

def my_view(request):
    filtered_objects = MyModel.objects.filter(field='value')
    return render(request, 'my_template.html', {'objects': filtered_objects})

def my_view(request):
    obj = MyModel.objects.get(id=1)
    obj.delete()
    return render(request, 'my_template.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
    
    from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('home')

from django.core.paginator import Paginator

def my_view(request):
    my_objects = MyModel.objects.all()
    paginator = Paginator(my_objects, 10)
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)
    return render(request, 'my_template.html', {'objects': page_objects})

from django.shortcuts import render, redirect
from .forms import MyForm

def upload_file(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MyForm()
    return render(request, 'upload.html', {'form': form})


from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)

    def clean_name(self):
        data = self.cleaned_data['name']
        # Perform custom validation logic
        if data == 'invalid':
            raise forms.ValidationError("Invalid name")
        return data