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
from home import views as home_views
from about import views as about_views
from resume import views as resume_views

urlpatterns = [
    path('',home_views.home, name='home'),
    path('hone/',home_views.home, name='home'),
    path('about-me/', about_views.about, name='about'),
    path('resume/', resume_views.resume, name='resume'),
    path('services/', core_views.services, name='services'),
    path('portfolio/', core_views.portfolio, name='portfolio'),
    path('portfolio-details/', core_views.portfolio_details, name='portfolio-details'),
    path('contact/', core_views.contact, name='contact'),
    path("admin/", admin.site.urls),
]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)