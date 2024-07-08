from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,'core/home.html')

def contact(request):
    return render(request,'core/contact.html')

def about(request):
    return render(request,'core/about.html')

def resume(request):
    return render(request,'core/resume.html')

def services(request):
    return render(request,'core/services.html')

def portfolio(request):
    return render(request,'core/portfolio.html')

def portfolio_details(request):
    return render(request,'core/portfolio-details.html')