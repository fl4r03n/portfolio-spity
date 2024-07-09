from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import os

class Home(models.Model):
    # Campos del modelo para la página de inicio
    titulo = models.CharField(_("Titulo"), max_length=100, default="SPITTER")
    descripcion = models.TextField(_("Descripcion"),default="I'm a professional content creator from Argentina")
    imagen_fondo = models.ImageField(_("Img Fondo"),upload_to='home/')
    # Otros campos según sea necesario

    def save(self, *args, **kwargs):
        if not self.pk and Home.objects.exists():
            raise ValueError('Solo puede existir una instancia de Home')
        return super(Home, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Home")
        verbose_name_plural = _("Home")

    def __str__(self):
        return self.titulo

@receiver(post_save, sender=Home)
def delete_old_background_image(sender, instance, **kwargs):
    # Obtener la última imagen (si existe)
    old_images = Home.objects.exclude(pk=instance.pk)
    for old_image in old_images:
        if os.path.isfile(old_image.background_image.path):
            os.remove(old_image.background_image.path)
    # Eliminar otros registros de la base de datos
    old_images.delete()

@receiver(pre_delete, sender=Home)
def delete_image_file(sender, instance, **kwargs):
    if os.path.isfile(instance.background_image.path):
        os.remove(instance.background_image.path)