from django.shortcuts import render, HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
# Create your views here.
@xframe_options_sameorigin
def portfolio(request):
    return render(request,'portfolio/portfolio.html')