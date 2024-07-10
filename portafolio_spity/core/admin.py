from django.contrib import admin

# Register your models here.
from .models import SiteConfiguration, SocialLinks

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not SiteConfiguration.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False


@admin.register(SocialLinks)
class SocialLinksAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not SocialLinks.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False