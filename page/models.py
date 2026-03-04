from django.db import models

# Create your models here.
from django.db import models

class SiteSettings(models.Model):
    """
    Global site settings (logo, contact info, etc.)
    """
    site_name = models.CharField(max_length=100, default="Terra Foods")
    logo = models.ImageField(upload_to='site/', blank=True, null=True, help_text="Company logo (recommended: 200x60px PNG)")
    favicon = models.ImageField(upload_to='site/', blank=True, null=True, help_text="Browser favicon (32x32px)")
    
    phone = models.CharField(max_length=20, default="+233 XXX XXX XXX")
    email = models.EmailField(default="info@terrafoods.com")
    whatsapp = models.CharField(max_length=20, default="233XXXXXXXXX", help_text="Without + sign")
    
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return "Site Settings"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj