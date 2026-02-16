from django.db import models
from django.utils.text import slugify

# Category Model (Main categories only)
class Category(models.Model):
    """
    Main product categories: Vegetables, Fruits, Herbs, Spices, Oils
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
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
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']


# Product Model (Simplified)
class Product(models.Model):
    """
    Simplified product model with only essential fields
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    description = models.TextField()
    
    # Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    
    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Inventory
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    
    # Media (Main image + 2 additional images)
    image = models.ImageField(upload_to='products/', blank=True, null=True, help_text="Main product image")
    image_2 = models.ImageField(upload_to='products/', blank=True, null=True, help_text="Additional image 1")
    image_3 = models.ImageField(upload_to='products/', blank=True, null=True, help_text="Additional image 2")
    
    # Product Details
    unit = models.CharField(max_length=50, default='piece', help_text="e.g., kg, bunch, liter, piece")
    
    # Features
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    
    # SEO Fields
    meta_title = models.CharField(max_length=200, blank=True, help_text="SEO title for Google")
    meta_description = models.CharField(max_length=300, blank=True, help_text="SEO description for Google")
    
    # Tracking
    views = models.IntegerField(default=0, help_text="Number of times product page was viewed")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """Auto-generate slug from name"""
        if not self.slug:
            self.slug = slugify(self.name)
        
        # Auto-generate SEO fields if empty
        if not self.meta_title:
            self.meta_title = f"{self.name} - Fresh Organic from Terra Foods"
        
        if not self.meta_description:
            self.meta_description = f"{self.description[:150]}..."
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']


# Product Review Model
class ProductReview(models.Model):
    """
    Customer reviews for products
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    review_text = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.product.name} ({self.rating}★)"
    
    class Meta:
        ordering = ['-created_at']