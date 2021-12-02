from django.shortcuts import render

# Create your views here.
def home(request):
    title= ' Home is working'
    return render(request, 'home.html', {'title':title})