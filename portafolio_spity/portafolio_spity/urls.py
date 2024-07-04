"""
URL configuration for portafolio_spity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('',core_views.home, name='home'),
    path('hone/',core_views.home, name='home'),
    path('about-me/', core_views.about, name='about'),
    path('resume/', core_views.resume, name='resume'),
    path('services/', core_views.services, name='services'),
    path('portfolio/', core_views.portfolio, name='portfolio'),
    path("admin/", admin.site.urls),
]
