from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.shortcuts import render, HttpResponse
from .models import SiteConfiguration, SocialLinks

def contact(request):
    return render(request,'core/contact.html')

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
    
def social_links(request):
    try:
        links = SocialLinks.objects.first()
    except SocialLinks.DoesNotExist:
        links = None
    return {
        'social_links': links
    }