from django.contrib import admin
from .models import Category, Product, ProductReview

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_available', 'is_featured', 'views', 'created_at']
    list_editable = ['price', 'stock', 'is_available', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}  # Fixed: auto-populate slug from 'name', not 'category'
    search_fields = ['name', 'description']
    list_filter = ['category', 'is_available', 'is_featured', 'created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'stock', 'is_available', 'unit')
        }),
        ('Images', {
            'fields': ('image', 'image_2', 'image_3'),
            'description': 'Upload product images here. Main image is required, others are optional.'
        }),
        ('Features', {
            'fields': ('is_featured',)
        }),
        ('SEO (Search Engine Optimization)', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
            'description': 'These fields are auto-generated but you can customize them for better Google rankings.'
        }),
    )
    
    readonly_fields = ['views']  # Make views read-only so admin can't accidentally change it


# Product Review Admin
@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'product', 'rating', 'is_approved', 'created_at']
    list_editable = ['is_approved']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['customer_name', 'product__name', 'review_text']
    readonly_fields = ['created_at']