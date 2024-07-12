from django.db import models
from django.utils.translation import gettext_lazy as _

class Education(models.Model):
    degree = models.CharField(_("Grado"), max_length=100)
    institution = models.CharField(_("Instituto"), max_length=100)
    start_year = models.IntegerField(_("Año inicio"))
    end_year = models.IntegerField(_("Año fin"), null=True, blank=True)
    description = models.TextField(_("Descripción"))
    
    class Meta:
        verbose_name = _("Educacion")
        verbose_name_plural = _("Educaciones")
        ordering = ['start_year']

    def __str__(self):
        return self.degree
    
class Experience(models.Model):
    title = models.CharField(_("Titulo"), max_length=100)
    company = models.CharField(_("Compañia"), max_length=100)
    start_year = models.IntegerField(_("Año inicio"))
    end_year = models.IntegerField(_("Año fin"), null=True, blank=True)  # null=True, blank=True if it's the current job
    description = models.TextField(_("Descripción"))
    responsibilities = models.TextField(_("Responsabilidades"))  # Store responsibilities as a comma-separated list or use another related model
    
    class Meta:
        verbose_name = _("Experiencia")
        verbose_name_plural = _("Experiencias")
        ordering = ['start_year']

    def __str__(self):
        return self.title

class ResumeDesc(models.Model):
    tittle_section = models.CharField(_("Título de Sección"), max_length=100, default="Resume")
    desc_section = models.TextField(_("Descripción de Sección"), default="Magnam dolores commodi suscipit...")

    def save(self, *args, **kwargs):
        if not self.pk and ResumeDesc.objects.exists():
            raise ValueError('Solo puede existir una instancia de ResumeDesc')
        return super(ResumeDesc, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Descripcion de Currículum")
        verbose_name_plural = _("Descripciones de Currículum")

    def __str__(self):
        return self.tittle_section