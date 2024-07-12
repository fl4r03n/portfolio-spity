from django.contrib import admin
from .models import Education, Experience, ResumeDesc

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_year', 'end_year')

@admin.register(ResumeDesc)
class ResumeDescAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not ResumeDesc.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False