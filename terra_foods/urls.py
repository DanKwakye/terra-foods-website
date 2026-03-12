"""
URL configuration for terra_foods project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products import views as product_views
from page import views as page_views
from sectors import views as sector_views
#from ai_agent import views as ai_views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Homepage & Products page
    path('', product_views.home, name='home'),
    path('products/', product_views.product_list, name='product_list'),
    path('products/<slug:product_slug>/', product_views.product_detail, name='product_detail'),

    #Static Pages
    path('about/', page_views.about, name='about'),
    path('contact/', page_views.contact, name='contact'),
    path('privacy-policy/', page_views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', page_views.terms_of_service, name='terms_of_service'),

    #Sectors
    path('sectors/<slug:sector_slug>/', sector_views.sector_detail, name='sector_detail'),

    #Ai Agent
    #path('api/chat', ai_views.chat, name='ai_chat')
    path('api/', include('ai_agent.urls')),

]



if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)