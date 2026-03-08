from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductReview

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'image_preview', 'product_count', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    search_fields = ['name', 'description']
    list_filter = ['is_active']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'icon', 'description')
        }),
        ('Product Page Description', {
            'fields': ('product_page_description',),
            'description': 'This description appears on the product list page when users click this category'
        }),
        ('Upload Image Here', {
            'fields': ('image',),
            'description': 'Click "Choose File" below, select an image, then click Save at the bottom'
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )
    
    def product_count(self, obj):
        count = obj.products.count()
        return format_html('<strong>{}</strong> products', count)
    product_count.short_description = 'Products'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return format_html('<span style="color: red;">❌ No image</span>')
    image_preview.short_description = 'Image'
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['slug']
        return []


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image_preview', 'unit', 'is_available', 'is_featured', 'views']
    list_editable = ['is_available', 'is_featured']
    search_fields = ['name', 'description']
    list_filter = ['category', 'is_available', 'is_featured', 'created_at']
    
    # REMOVED prepopulated_fields - causes conflict with readonly
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('📸 Upload Images Here (Up to 3)', {
            'fields': ('image', 'image_2', 'image_3'),
            'description': 'Click "Choose File" to upload product images'
        }),
        ('Details', {
            'fields': ('unit', 'is_available', 'is_featured')
        }),
        ('SEO (Auto-generated)', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
        ('Statistics', {
            'fields': ('views',),
            'classes': ('collapse',),
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return format_html('<span style="color: red;"> No image</span>')
    image_preview.short_description = 'Image'
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing existing - make slug readonly
            return ['slug', 'views', 'created_at']
        return ['views']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer_name', 'rating', 'is_approved', 'created_at']
    list_editable = ['is_approved']
    list_filter = ['is_approved', 'rating', 'created_at']
    search_fields = ['customer_name', 'customer_email', 'review_text']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Review Information', {
            'fields': ('product', 'customer_name', 'customer_email', 'rating', 'review_text')
        }),
        ('Moderation', {
            'fields': ('is_approved',)
        }),
    )