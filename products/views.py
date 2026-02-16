from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    """Homepage with featured products"""
    featured_products = Product.objects.filter(is_available=True, is_featured=True)[:8]
    categories = Category.objects.filter(is_active=True)
    
    context = {
        'products': featured_products,
        'categories': categories,
    }
    return render(request, 'home.html', context)


def product_list(request):
    """Product list with category filtering"""
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.filter(is_active=True)
    
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
    """Product detail page"""
    product = get_object_or_404(Product, slug=product_slug, is_available=True)
    
    # Increment view counter
    product.views += 1
    product.save(update_fields=['views'])
    
    # Get related products from same category
    related_products = Product.objects.filter(
        category=product.category,
        is_available=True
    ).exclude(id=product.id)[:4]
    
    # Get approved reviews
    reviews = product.reviews.filter(is_approved=True)
    
    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
    }
    return render(request, 'products/product_detail.html', context)