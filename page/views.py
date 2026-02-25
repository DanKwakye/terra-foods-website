from django.shortcuts import render

# Create your views here.
def about(request):
    """About page"""
    return render(request, 'pages/about.html')


def contact(request):
    """Contact page"""
    return render(request, 'pages/contact.html')