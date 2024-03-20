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
