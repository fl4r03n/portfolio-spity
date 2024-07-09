from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .models import Home
def home(request):
    home_context = Home.objects.last()
    return render(request,'home/home.html', {'home_context': home_context})