def about(request):
    return render(request,'about/about.html')

# Create your views here.
from django.shortcuts import render, HttpResponse
from .models import About
def about(request):
    about_context = About.objects.last()
    return render(request,'about/about.html', {'about_context': about_context})