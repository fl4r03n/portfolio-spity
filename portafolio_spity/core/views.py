from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.
from django.shortcuts import render, HttpResponse

def contact(request):
    return render(request,'core/contact.html')

def about(request):
    return render(request,'core/about.html')

def resume(request):
    return render(request,'core/resume.html')

def services(request):
    return render(request,'core/services.html')

@xframe_options_sameorigin
def portfolio(request):
    return render(request,'core/portfolio.html')

@xframe_options_sameorigin
def portfolio_details(request):
    return render(request,'core/portfolio-details.html')

def contact(request):
    return render(request,'core/contact.html')

from .models import SiteConfiguration

def site_configuration(request):
    # Obtener la configuración del sitio
    try:
        site_config = SiteConfiguration.objects.get()
    except SiteConfiguration.DoesNotExist:
        site_config = None

    # Retornar el contexto que deseas pasar a todas las plantillas
    return {
        'site_config': site_config
    }