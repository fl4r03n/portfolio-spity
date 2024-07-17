from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
import os
from core.models import validate_image_size


class About(models.Model):
    tittle_section = models.CharField(_("Título de Sección"), max_length=100, default="About")
    desc_section = models.TextField(_("Descripción de Sección"), default="Magnam dolores commodi suscipit...")

    # Información personal
    img = models.ImageField(_("Imagen"), upload_to='about/', default='about/default.jpg', validators=[validate_image_size])
    name = models.CharField(_("Nombre"), max_length=100, default="Content Creator, Video Editor, and Music Producer")
    desc_short = models.TextField(_("Descripción Corta"), default="Lorem ipsum dolor sit amet...")
    birthday = models.CharField(_("Cumpleaños"), max_length=100, default="1 May 1995")
    website = models.URLField(_("Sitio Web"), max_length=200, default="www.example.com")
    phone = models.CharField(_("Teléfono"), max_length=20, default="+123 456 7890")
    city = models.CharField(_("Ciudad"), max_length=100, default="New York, USA")
    age = models.IntegerField(_("Edad"), default=21)
    degree = models.CharField(_("Grado"), max_length=50, default="Master")
    email = models.EmailField(_("Email"), default="email@example.com")
    freelance = models.CharField(_("Freelance"), max_length=50, default="Available")
    desc_long = models.TextField(_("Descripción Larga"), default="Officiis eligendi itaque...")

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValueError('Solo puede existir una instancia de About')
        return super(About, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("About")

    def __str__(self):
        return self.tittle_section

@receiver(pre_save, sender=About)
def delete_old_imagen_about(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = About.objects.get(pk=instance.pk)
        except About.DoesNotExist:
            return
        if old_instance.img and old_instance.img != instance.img:
            if os.path.isfile(old_instance.img.path):
                os.remove(old_instance.img.path)

@receiver(pre_delete, sender=About)
def delete_image_file(sender, instance, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)

class SkillDesc(models.Model):
    tittle_section = models.CharField(_("Título de Sección"), max_length=100, default="Skills")
    desc_section = models.TextField(_("Descripción de Sección"), default="Magnam dolores commodi suscipit...")

    def save(self, *args, **kwargs):
        if not self.pk and SkillDesc.objects.exists():
            raise ValueError('Solo puede existir una instancia de SkillDesc')
        return super(SkillDesc, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Descripcion de Habilidades")
        verbose_name_plural = _("Descripciones de Habilidades")

    def __str__(self):
        return self.tittle_section

class Skill(models.Model):
    name = models.CharField(_("Nombre Habilidad"), max_length=100)
    percentage = models.IntegerField(_("Porcentaje"))

    class Meta:
        verbose_name = _("Habilidad")
        verbose_name_plural = _("Habilidades")

    def __str__(self):
        return self.name
    
class FactDesc(models.Model):
    tittle_section = models.CharField(_("Título de Sección"), max_length=100, default="Facts")
    desc_section = models.TextField(_("Descripción de Sección"), default="Magnam dolores commodi suscipit...")

    def save(self, *args, **kwargs):
        if not self.pk and FactDesc.objects.exists():
            raise ValueError('Solo puede existir una instancia de FactDesc')
        return super(FactDesc, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Descripcion de Datos")
        verbose_name_plural = _("Descripciones de Datos")

    def __str__(self):
        return self.tittle_section
    
class Fact(models.Model):
    title = models.CharField(_("Título del Dato"), max_length=100)
    end_value = models.IntegerField(_("Valor Final"), default=0)
    duration = models.IntegerField(_("Duración"), default=1)

    class Meta:
        verbose_name = _("Dato")
        verbose_name_plural = _("Datos")

    def __str__(self):
        return self.title

class TestimonialDesc(models.Model):
    tittle_section = models.CharField(_("Título de Sección"), max_length=100, default="Testimonials")
    desc_section = models.TextField(_("Descripción de Sección"), default="Magnam dolores commodi suscipit...")

    def save(self, *args, **kwargs):
        if not self.pk and TestimonialDesc.objects.exists():
            raise ValueError('Solo puede existir una instancia de TestimonialDesc')
        return super(TestimonialDesc, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Descripcion de Testimonios")
        verbose_name_plural = _("Descripciones de Testimonios")

    def __str__(self):
        return self.tittle_section
    
class Testimonial(models.Model):
    author_name = models.CharField(_("Nombre del autor"), max_length=100)
    author_position = models.CharField(_("Posición del autor"), max_length=100)
    testimonial_text = models.TextField(_("Texto del testimonio"))
    testimonial_image = models.ImageField(_("Imagen del testimonio"), upload_to='testimonials/', blank=True, null=True, validators=[validate_image_size])

    class Meta:
        verbose_name = _("Testimonio")
        verbose_name_plural = _("Testimonios")

    def __str__(self):
        return f"{self.author_name} - {self.author_position}"
    
@receiver(pre_save, sender=Testimonial)
def delete_old_imagen_testimonial(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Testimonial.objects.get(pk=instance.pk)
        except Testimonial.DoesNotExist:
            return
        if old_instance.testimonial_image and old_instance.testimonial_image != instance.testimonial_image:
            if os.path.isfile(old_instance.testimonial_image.path):
                os.remove(old_instance.testimonial_image.path)

@receiver(pre_delete, sender=Testimonial)
def delete_image_file_testimonial(sender, instance, **kwargs):
    if instance.testimonial_image:
        if os.path.isfile(instance.testimonial_image.path):
            os.remove(instance.testimonial_image.path)