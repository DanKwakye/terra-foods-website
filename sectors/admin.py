from django.contrib import admin
from .models import Sector

# Register your models here.
@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'tagline', 'description', 'hero_image')
        }),
        ('Benefits', {
            'fields': (
                'benefit_1_title', 'benefit_1_description',
                'benefit_2_title', 'benefit_2_description',
                'benefit_3_title', 'benefit_3_description',
            )
        }),
        ('Call to Action', {
            'fields': ('cta_text',)
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )