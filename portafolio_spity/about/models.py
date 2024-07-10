from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
import os

class About(models.Model):
    tittle_section = models.CharField(_("Título de Sección"), max_length=100, default="About")
    desc_section = models.TextField(_("Descripción de Sección"), default="Magnam dolores commodi suscipit...")

    # Información personal
    img = models.ImageField(_("Imagen"), upload_to='about/', default='about/default.jpg')
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