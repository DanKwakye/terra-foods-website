from django.core.management.base import BaseCommand
from sectors.models import Sector

class Command(BaseCommand):
    help = 'Load sample sectors - minimal content'

    def handle(self, *args, **kwargs):
        sectors_data = [
            {
                'name': 'Hotels',
                'hero_title': 'Fresh Produce for Hotels',
                'hero_subtitle': 'Quality ingredients delivered daily to elevate your guest dining experience',
                'content': '''We understand the demands of hotel kitchens. Fresh, reliable supplies are essential to maintaining your reputation for excellence.

Terra Foods provides hotels across Accra with premium organic produce, delivered on your schedule. From breakfast buffets to fine dining restaurants, we ensure your kitchen always has the freshest ingredients.

Our dedicated account managers work with your procurement team to ensure seamless ordering and delivery. Volume discounts available for regular orders.

Contact us to discuss your hotel's specific requirements and delivery schedule.''',
                'order': 1,
            },
            {
                'name': 'Restaurants',
                'hero_title': 'Fresh Ingredients for Restaurants',
                'hero_subtitle': 'Reliable daily deliveries of premium produce for discerning chefs',
                'content': '''Your menu deserves the best. We supply restaurants across Accra with farm-fresh organic produce that meets the exacting standards of professional kitchens.

From fine dining establishments to casual eateries, our extensive selection ensures you have exactly what you need, when you need it.

Flexible delivery schedules accommodate your kitchen prep times. Early morning deliveries available. Consistent quality you can count on, day after day.

Special pricing for restaurant partnerships. Contact us to set up your account.''',
                'order': 2,
            },
            {
                'name': 'Executive Chefs',
                'hero_title': 'Premium Produce for Executive Chefs',
                'hero_subtitle': 'Hand-selected ingredients worthy of your culinary vision',
                'content': '''As an executive chef, you demand excellence. We deliver it.

Terra Foods works directly with executive chefs across Accra, providing access to premium organic produce that meets professional standards.

We understand seasonality, quality markers, and the importance of consistency. Our team personally selects produce to ensure it meets your specifications.

Need something special? We source unique ingredients upon request. Direct communication with our procurement team ensures your requirements are always met.

Contact us to discuss your kitchen's needs.''',
                'order': 3,
            },
            {
                'name': 'Event Catering',
                'hero_title': 'Fresh Produce for Event Catering',
                'hero_subtitle': 'Large-volume orders delivered on time, every time',
                'content': '''Event catering requires precision timing and reliable suppliers. We deliver both.

Terra Foods specializes in large-volume orders for weddings, corporate events, conferences, and special occasions. From intimate gatherings to events serving hundreds, we ensure you have the fresh produce you need.

Advanced ordering ensures availability. Delivery scheduled to match your event prep timeline. Volume pricing for large orders.

Our team works with you to plan quantities and ensure nothing is overlooked.

Contact us to discuss your upcoming event requirements.''',
                'order': 4,
            },
            {
                'name': 'Corporate',
                'hero_title': 'Fresh Produce for Corporate Offices',
                'hero_subtitle': 'Healthy options for your workplace cafeteria and staff kitchens',
                'content': '''Keep your team healthy and productive with fresh organic produce delivered to your office.

Terra Foods supplies corporate cafeterias, executive lounges, and staff kitchens across Accra. Regular deliveries ensure your team always has access to healthy, fresh options.

Perfect for companies prioritizing employee wellness. Custom orders available for special dietary requirements or preferences.

Flexible delivery schedules work around your office hours. Invoicing and account management designed for corporate procurement processes.

Contact us to set up your corporate account.''',
                'order': 5,
            },
        ]
        
        created = 0
        for sector_data in sectors_data:
            sector, is_created = Sector.objects.get_or_create(
                name=sector_data['name'],
                defaults={
                    'tagline': sector_data.get("hero_title"),
                    'description': sector_data.get("content"),
                    'order': sector_data.get("order", 0),
                    'is_active': True,
                }
            )
            if is_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f'✓ {sector.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ {sector.name}'))

        self.stdout.write(self.style.SUCCESS(f'\n Created {created} sectors!'))