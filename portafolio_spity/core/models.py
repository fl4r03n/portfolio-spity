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
    
class SocialLinks(models.Model):
    link_social = models.CharField(_("Redes"), max_length=300, default="#")
    link_x = models.CharField(_("X"), max_length=300, default="#")
    link_fb = models.CharField(_("Facebook"), max_length=300, default="#")
    link_ig = models.CharField(_("Instagram"), max_length=300, default="#")
    link_in = models.CharField(_("Linkedin"), max_length=300, default="#")
    link_tw = models.CharField(_("Twitch"), max_length=300, default="#")
    link_yt = models.CharField(_("YouTube"), max_length=300, default="#")
    link_sc = models.CharField(_("SoundCloud"), max_length=300, default="#")
    
    
    def save(self, *args, **kwargs):
        if not self.pk and SocialLinks.objects.exists():
            raise ValueError('Solo puede existir una instancia de SocialLinks')
        return super(SocialLinks, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Social Links")
        verbose_name_plural = _("Social Links")
    
    def __str__(self):
        return self.link_social