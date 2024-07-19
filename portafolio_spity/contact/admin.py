from django.contrib import admin

from .models import ContactInfo


# Register your models here.
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not ContactInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False
