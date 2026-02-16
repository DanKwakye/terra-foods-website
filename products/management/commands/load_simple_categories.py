from django.core.management.base import BaseCommand
from products.models import Category

class Command(BaseCommand):
    help = 'Loads simplified categories'

    def handle(self, *args, **kwargs):
        categories_data = [
            {
                'name': 'Vegetables',
                'icon': '🥬 🥒',
                'description': 'Fresh organic vegetables from local farms',
                'order': 1,
            },
            {
                'name': 'Fruits',
                'icon': '🍇',
                'description': 'Sweet, juicy fruits picked at peak ripeness',
                'order': 2,
            },
            {
                'name': 'Herbs',
                'icon': '🌿',
                'description': 'Aromatic fresh herbs for cooking and garnishing',
                'order': 3,
            },
            {
                'name': 'Spices',
                'icon': '🧄',
                'description': 'Fresh spices and aromatics for authentic flavors',
                'order': 4,
            },
            {
                'name': 'Oils',
                'icon': '🫒',
                'description': 'Pure, virgin oils for cooking and wellness',
                'order': 5,
            },
            {
                "name": "Eggs",
                "icon": "🥚",
                "description": 'Farm fresh eggs supplied in bulk for hotels, restaurants, and catering services.',
                'order': 5,
            },
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Created: {category.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'○ Exists: {category.name}'))
        
        self.stdout.write(self.style.SUCCESS('\n Categories loaded!'))