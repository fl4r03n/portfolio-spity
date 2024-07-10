from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, post_save, pre_delete
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

@receiver(pre_save, sender=Home)
def delete_old_imagen_fondo(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Home.objects.get(pk=instance.pk)
        except Home.DoesNotExist:
            return
        if old_instance.imagen_fondo and old_instance.imagen_fondo != instance.imagen_fondo:
            if os.path.isfile(old_instance.imagen_fondo.path):
                os.remove(old_instance.imagen_fondo.path)

@receiver(pre_delete, sender=Home)
def delete_image_file(sender, instance, **kwargs):
    if instance.imagen_fondo:
        if os.path.isfile(instance.imagen_fondo.path):
            os.remove(instance.imagen_fondo.path)