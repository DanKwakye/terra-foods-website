from django.shortcuts import render

# Create your views here.
def about(request):
    """About page"""
    return render(request, 'pages/about.html')


def contact(request):
    """Contact page"""
    return render(request, 'pages/contact.html')

def privacy_policy(request):
    """Privacy Policy page"""
    return render(request, 'pages/privacy_policy.html')


def terms_of_service(request):
    """Terms of Service page"""
    return render(request, 'pages/terms_of_service.html')