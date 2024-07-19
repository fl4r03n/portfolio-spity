from django.contrib import admin

from .models import (
    About,
    Fact,
    FactDesc,
    Skill,
    SkillDesc,
    Testimonial,
    TestimonialDesc,
)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not About.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False


@admin.register(SkillDesc)
class SkillDescAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not SkillDesc.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage")


@admin.register(FactDesc)
class FactDescAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not FactDesc.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ("title", "end_value", "duration")

    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existen 4 registros
        if Fact.objects.count() >= 4:
            return False
        return True


@admin.register(TestimonialDesc)
class TestimonialDescAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not TestimonialDesc.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "author_position")
