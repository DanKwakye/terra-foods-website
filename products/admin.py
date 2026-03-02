from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductReview

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'image_preview', 'product_count', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_filter = ['is_active']
    
    fieldsets = (
        (' EDITING EXISTING CATEGORY', {
            'description': 'You are editing an existing category. DO NOT change the name unless you want to rename it.',
            'fields': ('name', 'slug')
        }),
        ('Category Details', {
            'fields': ('icon', 'description')
        }),
        (' Upload Image Here', {
            'fields': ('image',),
            'description': 'Click "Choose File" below to upload an image for this category'
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )
    
    def product_count(self, obj):
        """Show number of products"""
        count = obj.products.count()
        return format_html('<strong>{}</strong> products', count)
    product_count.short_description = 'Products'
    
    def image_preview(self, obj):
        """Show small image preview"""
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return ' No image'
    image_preview.short_description = 'Image'
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing existing
            return ['slug']
        return []


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image_preview', 'unit', 'is_available', 'is_featured', 'views']
    list_editable = ['is_available', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    list_filter = ['category', 'is_available', 'is_featured', 'created_at']
    
    fieldsets = (
        (' EDITING EXISTING PRODUCT', {
            'description': 'You are editing an existing product. DO NOT change the name unless renaming.',
            'fields': ('name', 'slug')
        }),
        ('Product Details', {
            'fields': ('category', 'description', 'unit')
        }),
        (' Upload Images Here (Up to 3)', {
            'fields': ('image', 'image_2', 'image_3'),
            'description': 'Click "Choose File" to upload product images'
        }),
        ('Settings', {
            'fields': ('is_available', 'is_featured')
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
    
    readonly_fields = ['views', 'created_at']
    
    def image_preview(self, obj):
        """Show small image preview"""
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return ' No image'
    image_preview.short_description = 'Image'
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['slug', 'views', 'created_at']
        return ['views']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer_name', 'rating', 'is_approved', 'created_at']
    list_editable = ['is_approved']
    list_filter = ['is_approved', 'rating', 'created_at']
    search_fields = ['customer_name', 'customer_email', 'review_text']