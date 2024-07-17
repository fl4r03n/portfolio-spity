from django.contrib import admin
from .models import PortfolioDesc, PortfolioItem

# Register your models here.
@admin.register(PortfolioDesc)
class PortfolioDescAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not PortfolioDesc.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False
    
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'project_date')
    search_fields = ('title', 'category', 'client')
    fieldsets = (None, {
            'fields': ('title', 'category', 'description', 'image1', 'image2', 'image3', 'client', 'project_date', 'project_url'),
            'description': 'Available categories: Audio, Video, Otros.'
        }),