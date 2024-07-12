from django.db import models
from django.utils.translation import gettext_lazy as _

class Education(models.Model):
    degree = models.CharField(_("Grado"), max_length=100)
    institution = models.CharField(_("Instituto"), max_length=100)
    start_year = models.IntegerField(_("Año inicio"))
    end_year = models.IntegerField(_("Año fin"))
    description = models.TextField(_("Descripción"))
    
    class Meta:
        verbose_name = _("Educacion")
        verbose_name_plural = _("Educaciones")

    def __str__(self):
        return self.degree
    
class Experience(models.Model):
    title = models.CharField(_("Titulo"), max_length=100)
    company = models.CharField(_("Compañia"), max_length=100)
    start_year = models.IntegerField(_("Año inicio"))
    end_year = models.IntegerField(_("Año fin"), null=True, blank=True)  # null=True, blank=True if it's the current job
    description = models.TextField(_("Descripción"))
    responsibilities = models.TextField(_("Responsabilidades"))  # Store responsibilities as a comma-separated list or use another related model

    def __str__(self):
        return self.title