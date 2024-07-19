import os

from core.models import validate_image_size
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class PortfolioDesc(models.Model):
    tittle_section = models.CharField(
        _("Título de Sección"), max_length=100, default="Portfolio"
    )
    desc_section = models.TextField(
        _("Descripción de Sección"), default="Magnam dolores commodi suscipit..."
    )

    def save(self, *args, **kwargs):
        if not self.pk and PortfolioDesc.objects.exists():
            raise ValueError("Solo puede existir una instancia de PortfolioDesc")
        return super(PortfolioDesc, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Descripcion de Portafolio")
        verbose_name_plural = _("Descripciones de Portafolio")

    def __str__(self):
        return self.tittle_section


class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [("Audio", "Audio"), ("Video", "Video"), ("Otros", "Otros")]
    title = models.CharField(_("Titulo del Proyecto"), max_length=100)
    category = models.CharField(
        _("Tipo de Filtro"), max_length=50, choices=CATEGORY_CHOICES
    )
    description = models.TextField(_("Descripcion del Proyecto"))
    image1 = models.ImageField(
        _("Imagen 1"), upload_to="portfolio/", validators=[validate_image_size]
    )
    image2 = models.ImageField(
        _("Imagen 2"),
        upload_to="portfolio/",
        blank=True,
        null=True,
        validators=[validate_image_size],
    )
    image3 = models.ImageField(
        _("Imagen 3"),
        upload_to="portfolio/",
        blank=True,
        null=True,
        validators=[validate_image_size],
    )
    client = models.CharField(_("Cliente"), max_length=100)
    project_date = models.DateField(_("Fecha"))
    project_url = models.URLField(_("Link"), blank=True, null=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=PortfolioItem)
def delete_old_images_PortfolioItem(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = PortfolioItem.objects.get(pk=instance.pk)
        except PortfolioItem.DoesNotExist:
            return
        if old_instance.image1 and old_instance.image1 != instance.image1:
            if os.path.isfile(old_instance.image1.path):
                os.remove(old_instance.image1.path)
        if old_instance.image2 and old_instance.image2 != instance.image2:
            if os.path.isfile(old_instance.image2.path):
                os.remove(old_instance.image2.path)
        if old_instance.image3 and old_instance.image3 != instance.image3:
            if os.path.isfile(old_instance.image3.path):
                os.remove(old_instance.image3.path)


@receiver(pre_delete, sender=PortfolioItem)
def delete_image_files_PortfolioItem(sender, instance, **kwargs):
    if instance.image1:
        if os.path.isfile(instance.image1.path):
            os.remove(instance.image1.path)
    if instance.image2:
        if os.path.isfile(instance.image2.path):
            os.remove(instance.image2.path)
    if instance.image3:
        if os.path.isfile(instance.image3.path):
            os.remove(instance.image3.path)
