from django.contrib import admin

from .models import Home

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not Home.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False
#    pass   O define configuraciones específicas aquí