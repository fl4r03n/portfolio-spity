from django.db import models
from django.utils.translation import gettext_lazy as _


class ServicesDesc(models.Model):
    tittle_section = models.CharField(
        _("Título de Sección"), max_length=100, default="Services"
    )
    desc_section = models.TextField(
        _("Descripción de Sección"), default="Magnam dolores commodi suscipit..."
    )

    def save(self, *args, **kwargs):
        if not self.pk and ServicesDesc.objects.exists():
            raise ValueError("Solo puede existir una instancia de ServicesDesc")
        return super(ServicesDesc, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Descripcion de Servicios")
        verbose_name_plural = _("Descripciones de Servicios")

    def __str__(self):
        return self.tittle_section


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(
        max_length=50,
        default="youtube",
        help_text=(
            "Nombre del ícono (ej. youtube). "
            "Visita https://boxicons.com para ver la lista completa de íconos."
        ),
    )
    icon_color = models.CharField(
        max_length=50,
        default="darkred",
        help_text=(
            "Colores disponibles: orange, yellow, pink, black, silver, gray, white, maroon, "
            "red, purple, fuchsia, green, lime, olive, yellow, navy, blue, teal, aqua"
        ),
    )

    class Meta:
        verbose_name = _("Servicio")
        verbose_name_plural = _("Servicios")

    def __str__(self):
        return self.title
