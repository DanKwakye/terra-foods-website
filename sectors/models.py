from django.db import models
from django.utils.text import slugify

class  Sector(models.Model):
    """
    Business sectors we serve (Hotels, Restaurants, Corporate, etc.)
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    tagline = models.CharField(max_length=200, help_text="Short catchy phrase")
    description = models.TextField()
    
    hero_image = models.ImageField(upload_to='sectors/', blank=True, null=True)
    
    # Benefits section
    benefit_1_title = models.CharField(max_length=100, blank=True)
    benefit_1_description = models.TextField(blank=True)
    
    benefit_2_title = models.CharField(max_length=100, blank=True)
    benefit_2_description = models.TextField(blank=True)
    
    benefit_3_title = models.CharField(max_length=100, blank=True)
    benefit_3_description = models.TextField(blank=True)

    #Testimonial (Updated List)
    class Sector(models.Model):
        name = models.CharField(max_length=200)
        slug = models.SlugField(unique=True)
        tagline = models.CharField(max_length=255, blank=True)
        description = models.TextField(blank=True)
        hero_image = models.ImageField(upload_to="sector/", blank=True, null=True)
        is_active = models.BooleanField(default=True)

        def __str__(self):
            return self.name
    
    # CTA
    cta_text = models.CharField(max_length=255, default="Contact Our Team Today, Reach out to our helpful team today with any questions you may have to discuss your fruit and vegetable supply needs.We are more than happy to assist with any questions you may have. Source only the best in high-quality vegetables for your customers today!")
    
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']



#updated list
class SectorFeatureSection(models.Model):
    sector = models.ForeignKey(
        Sector,
        related_name="feature_sections",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.title}"

# Create your models here.
