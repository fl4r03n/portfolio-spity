from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactInfo(models.Model):
    tittle_section = models.CharField(_("Título de Sección"), max_length=100, default="Contact Information")
    desc_section = models.TextField(_("Descripción de Sección"), default="Aquí puede encontrar mi información de contacto...")
    location = models.CharField(_("Ubicación"), max_length=255, default="Argentina")
    email = models.EmailField(_("Correo Electrónico"), default="contact.spitterworld@gmail.com")
    call = models.CharField(_("Teléfono"), max_length=20, default="No especificado")

    def save(self, *args, **kwargs):
        if not self.pk and ContactInfo.objects.exists():
            raise ValueError('Solo puede existir una instancia de ContactInfo')
        return super(ContactInfo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Información de Contacto")
        verbose_name_plural = _("Información de Contacto")

    def __str__(self):
        return self.tittle_section