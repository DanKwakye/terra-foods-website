from django.contrib import admin
from django.utils.html import format_html
from .models import Sector

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'hero_h1', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['name', 'hero_h1']
    list_filter = ['is_active']
    
   
    
    fieldsets = (
        ('Basic Settings', {
            'fields': ('name', 'slug', 'is_active', 'order', 'meta_description')
        }),
        ('SECTION 1: Hero (Text Left, Image Right)', {
            'fields': ('hero_h1', 'hero_paragraph_1', 'hero_paragraph_2', 'hero_paragraph_3', 'hero_cta_text', 'hero_image'),
            'classes': ('collapse',),
        }),
        ('SECTION 2: Trust (Centered)', {
            'fields': ('trust_h2', 'trust_paragraph', 'trust_cta_text'),
            'classes': ('collapse',),
        }),
        ('SECTION 3: Split Left (Image Left, Text Right)', {
            'fields': ('split_left_h2', 'split_left_content', 'split_left_cta_text', 'split_left_image'),
            'classes': ('collapse',),
        }),
        ('SECTION 4: Split Right (Text Left, Image Right)', {
            'fields': ('split_right_h2', 'split_right_content', 'split_right_cta_text', 'split_right_image'),
            'classes': ('collapse',),
        }),
        ('SECTION 5: Operations (Centered)', {
            'fields': ('operations_h2', 'operations_content'),
            'classes': ('collapse',),
        }),
        ('SECTION 6: Partner (Text Left, Image Right)', {
            'fields': ('partner_h2', 'partner_content', 'partner_cta_text', 'partner_image'),
            'classes': ('collapse',),
        }),
        ('SECTION 7: Dark CTA (Full-width)', {
            'fields': ('dark_cta_h2', 'dark_cta_paragraph', 'dark_cta_button_text', 'dark_cta_image'),
            'classes': ('collapse',),
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing existing - make slug readonly
            return ['slug']
        return []