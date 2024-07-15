from django.shortcuts import render
from .models import ServicesDesc, Service

def services(request):
    services_desc = ServicesDesc.objects.last()
    services = Service.objects.all()
    return render(request,'services/services.html',
                  {"services_desc": services_desc,
                  "services": services})