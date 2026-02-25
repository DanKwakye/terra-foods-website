from django.shortcuts import render, get_object_or_404
from .models import Sector
from products.views import Product

# Create your views here.
#def sector_detail(request, sector_slug):
 #   """
 #   Sector detail page - minimal and clean
 #   """
  #  sector = get_object_or_404(Sector, slug=sector_slug, is_active=True)
   # return render(request, "sectors/sectors_detail.html", {"sector": sector})

   #old view
    #Sector  = get_object_or_404(Sector, slug=sector_slug, is_active=True)

    #context = {
    #    'sector': sector,
    #}
    #return render(request, 'sectors/sector_detail.html', context)

    #def sector_detail(request, sector_slug):

#UPDATED VIEW
def sector_detail(request, sector_slug):
    sector = get_object_or_404(Sector, slug=sector_slug, is_active=True)


    #Example: get feature products for that scetor
    products = Product.objects.filter(is_featured=True)[:8]

    context = {
        "sector": sector,
        "products": products,
    }

    return render(request, "sectors/sectors_detail.html", context)
        