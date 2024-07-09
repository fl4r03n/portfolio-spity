from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteConfiguration(models.Model):
    site_name = models.CharField(_("Nombre Sitio"), max_length=100, default="SPITTER")
    footer_text = models.CharField(_("Copyright"), max_length=255, default="© Copyright Spitty. All Rights Reserved")
    
    
    def save(self, *args, **kwargs):
        if not self.pk and SiteConfiguration.objects.exists():
            raise ValueError('Solo puede existir una instancia de SiteConfiguration')
        return super(SiteConfiguration, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Config")
        verbose_name_plural = _("Configs")
    
    def __str__(self):
        return self.site_name
    
