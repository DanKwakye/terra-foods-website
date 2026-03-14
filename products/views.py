from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Category, Product
import random
from datetime import datetime
from django.db import models
from django.core.cache import cache

def home(request):
    """
    Homepage with weekly featured products (5 random with category diversity)
    """
    categories = Category.objects.filter(is_active=True).only('id', 'name', 'slug', 'icon', 'image' )
    
    # Get 5 featured products for this week
    # Prioritize different categories for diversity
    featured_products = get_weekly_featured_products()
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
    }
    return render(request, 'home.html', context)


def get_weekly_featured_products():
    """
    Get 5 featured products for the week with category diversity
    Changes every Monday (week starts on Monday)
    """
    # Get current week number (changes every Monday)
    today = datetime.now()
    week_number = today.isocalendar()[1]  # ISO week number
    
    # Use week number as seed for consistent results during the week
    random.seed(week_number)
    
    # Get all available products grouped by category
    all_products = list(Product.objects.filter(is_available=True).select_related('category')
                        .only('id', 'name', 'slug', 'image', 'category__name', 'category__icon'))
    
    if not all_products:
        return []
    
    # Try to get one product from each category first (for diversity)
    categories = Category.objects.filter(is_active=True)
    featured = []
    used_categories = set()
    
    for category in categories:
        category_products = [p for p in all_products if p.category == category and p.category not in used_categories]
        if category_products and len(featured) < 5:
            product = random.choice(category_products)
            featured.append(product)
            used_categories.add(category)
    
    # If we still need more products, pick random ones
    while len(featured) < 5 and len(all_products) > len(featured):
        remaining = [p for p in all_products if p not in featured]
        if remaining:
            featured.append(random.choice(remaining))
        else:
            break
    
    # Reset random seed
    random.seed()
    
    return featured[:5]


def product_list(request):
    # Try to get from cache first
    cache_key = f'product_list_{category_slug if category_slug else "all"}'
    products = cache.get(cache_key)
    
    if not products:
        # If not in cache, query database
        products = Product.objects.filter(is_available=True).select_related('category')
        if category_slug:
            products = products.filter(category__slug=category_slug)
        
        # Cache for 10 minutes
        cache.set(cache_key, products, 600)

    """
    Product list with category filtering
    """
    products = Product.objects.filter(is_available=True).select_related('category')
    categories = Category.objects.filter(is_active=True).annotate(product_count=Count('products', filter=models.Q(products__is_available=True)))
    
    current_category = None
    category_slug = request.GET.get('category')
    
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug, is_active=True)
        products = products.filter(category=current_category)
    
    # Quick filter: featured products
    if request.GET.get('featured') == 'true':
        products = products.filter(is_featured=True)
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': current_category,
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, product_slug):
    """
    Product detail page
    """
    product = get_object_or_404(
        Product.objects.select_related('category'),
        slug=product_slug,
        is_available=True)
    
    # Increment view counter
    Product.objects.filter(id=product.id).update(views=models.F('views') + 1)
    product.refresh_from_db()
    #product.views += 1
    #product.save(update_fields=['views'])
    
    # Get related products from same category
    related_products = Product.objects.filter(
        category=product.category,
        is_available=True
    ).exclude(id=product.id).select_related('category')[:4]
    
    # Get approved reviews
    reviews = product.reviews.filter(is_approved=True).order_by('-created_at')
    
    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
    }
    return render(request, 'products/product_detail.html', context)