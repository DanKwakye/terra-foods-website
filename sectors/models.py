from django.db import models
from django.utils.text import slugify

class Sector(models.Model):
    """
    7-section sector model matching Urban Grocer structure exactly
    """
    name = models.CharField(max_length=100, help_text="e.g., Hotels")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    # ============ SECTION 1: HERO (Split - Text Left, Image Right) ============
    hero_h1 = models.CharField(max_length=200, help_text="Main headline")
    hero_paragraph_1 = models.TextField(help_text="First strong paragraph")
    hero_paragraph_2 = models.TextField(help_text="Second strong paragraph")
    hero_paragraph_3 = models.TextField(help_text="Third strong paragraph")
    hero_cta_text = models.CharField(max_length=100, default="Request Supply Quote")
    hero_image = models.ImageField(upload_to='sectors/hero/', blank=True, null=True, help_text="Right side image - hotel kitchen/professional setting")
    
    # ============ SECTION 2: TRUST (Centered) ============
    trust_h2 = models.CharField(max_length=200, help_text="Trust section headline")
    trust_paragraph = models.TextField(help_text="Main trust paragraph covering local sourcing, delivery, etc.")
    trust_cta_text = models.CharField(max_length=100, default="Speak to Our Supply Team")
    
    # ============ SECTION 3: SPLIT LEFT (Image Left, Text Right) ============
    split_left_h2 = models.CharField(max_length=200, help_text="Headline for left split section")
    split_left_content = models.TextField(help_text="Content about seasonal produce, local farms, quality control")
    split_left_cta_text = models.CharField(max_length=100, default="Learn More")
    split_left_image = models.ImageField(upload_to='sectors/split/', blank=True, null=True, help_text="Fresh produce crates/hotel kitchen")
    
    # ============ SECTION 4: SPLIT RIGHT (Text Left, Image Right) ============
    split_right_h2 = models.CharField(max_length=200, help_text="Headline for right split section")
    split_right_content = models.TextField(help_text="Content about time-saving, pre-cut vegetables, bulk supply")
    split_right_cta_text = models.CharField(max_length=100, default="Get Started")
    split_right_image = models.ImageField(upload_to='sectors/split/', blank=True, null=True, help_text="Chef preparing food")
    
    # ============ SECTION 5: OPERATIONS (Centered) ============
    operations_h2 = models.CharField(max_length=200, help_text="Operations headline")
    operations_content = models.TextField(help_text="Content about scheduled delivery, inventory, emergency supply, account managers")
    
    # ============ SECTION 6: PARTNER SPLIT (Text Left, Image Right) ============
    partner_h2 = models.CharField(max_length=200, help_text="Partnership headline")
    partner_content = models.TextField(help_text="Why partner with Terra Foods")
    partner_cta_text = models.CharField(max_length=100, default="Become a Partner")
    partner_image = models.ImageField(upload_to='sectors/partner/', blank=True, null=True, help_text="Premium produce display")
    
    # ============ SECTION 7: DARK CTA (Full-width with overlay) ============
    dark_cta_h2 = models.CharField(max_length=200, help_text="Final CTA headline")
    dark_cta_paragraph = models.TextField(help_text="Final compelling paragraph")
    dark_cta_button_text = models.CharField(max_length=100, default="Request Quote")
    dark_cta_image = models.ImageField(upload_to='sectors/cta/', blank=True, null=True, help_text="Fresh vegetables close-up background")
    
    # Meta
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    meta_description = models.CharField(max_length=160, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        if not self.meta_description and self.hero_paragraph_1:
            self.meta_description = self.hero_paragraph_1[:155] + '...'
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']