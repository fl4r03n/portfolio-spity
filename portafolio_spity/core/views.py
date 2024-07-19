from .models import SiteConfiguration, SocialLinks


def site_configuration(request):
    # Obtener la configuración del sitio
    try:
        site_config = SiteConfiguration.objects.get()
    except SiteConfiguration.DoesNotExist:
        site_config = None

    # Retornar el contexto que deseas pasar a todas las plantillas
    return {"site_config": site_config}


def social_links(request):
    try:
        links = SocialLinks.objects.first()
    except SocialLinks.DoesNotExist:
        links = None
    return {"social_links": links}
