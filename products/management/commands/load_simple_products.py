from django.core.management.base import BaseCommand
from django.utils.text import slugify
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Loads simplified products'

    def handle(self, *args, **kwargs):
        # Get categories
        try:
            vegetables = Category.objects.get(name='Vegetables')
            fruits = Category.objects.get(name='Fruits')
            herbs = Category.objects.get(name='Herbs')
            spices = Category.objects.get(name='Spices')
            oils = Category.objects.get(name='Oils')
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR('Categories not found! Run load_simple_categories first.'))
            return
        categories = {cat.name: cat for cat in Category.objects.all()}


        products_data = [
    {
      "name": "Fresh Eggs",
      "description": "Farm fresh eggs supplied in bulk for hotels, restaurants, and catering services.",
      "category": "Eggs",
      "is_available": True      
    },

    #VEGETABLE
    {
      "name": "Tomatoes",
      "description": "Fresh ripe tomatoes sourced for daily kitchen operations.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Cherry Tomatoes",
      "description": "Premium cherry tomatoes ideal for salads and garnishing.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Green Chilli Pepper",
      "description": "Fresh green chilli peppers for spice and flavor.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Carrots",
      "description": "Fresh crunchy carrots suitable for cooking and salads.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Cabbage",
      "description": "High-quality cabbage supplied fresh.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Onion (White & Red)",
      "description": "Fresh white and red onions for all culinary needs.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Cucumber",
      "description": "Fresh cucumbers ideal for salads and side dishes.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Lettuce",
      "description": "Fresh lettuce supplied daily for kitchens.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Romain Lettuce",
      "description": "Crisp romain lettuce for premium salads.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Iceberg Lettuce",
      "description": "Fresh iceberg lettuce with crisp texture.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Bell Pepper (Green, Yellow & Red)",
      "description": "Colorful fresh bell peppers supplied in bulk.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Garlic",
      "description": "Fresh garlic bulbs for seasoning and cooking.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Irish Potatoes",
      "description": "Fresh Irish potatoes for bulk kitchen use.",
      "category": "Vegetables",
      "is_available": True
    },
    {
      "name": "Aubergine",
      "description": "Fresh aubergine (eggplant) supplied in bulk.",
      "category": "Vegetables",
      "is_available": True
    },

    #FRUITS
    {
      "name": "Pineapple",
      "description": "Sweet and fresh pineapples sourced locally.",
      "category": "Fruits",
      "is_available": True
    },
    {
      "name": "Mango",
      "description": "Fresh mangoes supplied for hotels and catering services.",
      "category": "Fruits",
      "is_available": True
    },
    {
      "name": "Banana",
      "description": "Fresh bananas suitable for breakfast service and smoothies.",
      "category": "Fruits",
      "is_available": True
    },
    {
      "name": "Lemon",
      "description": "Fresh lemons ideal for beverages and seasoning.",
      "category": "Fruits",
      "is_available": True
    },
    {
      "name": "Pawpaw",
      "description": "Fresh pawpaw supplied in bulk.",
      "category": "Fruits",
      "is_available": True
    },
    {
      "name": "Watermelon",
      "description": "Fresh watermelons ideal for buffet and juice service.",
      "category": "Fruits",
      "is_available": True
    },
    {
      "name": "Avocado Pear",
      "description": "Premium avocado pears supplied fresh.",
      "category": "Fruits",
      "is_available": True
    },
    {
      "name": "Strawberry",
      "description": "Fresh strawberries for desserts and garnishing.",
      "category": "Fruits",
      "is_available": True
    },
    {
      "name": "Apple",
      "description": "Fresh apples supplied for catering and hospitality services.",
      "category": "Fruits",
      "is_available": True
    },
    {
      "name": "Grapes",
      "description": "Fresh grapes ideal for buffet and dessert service.",
      "category": "Fruits",
      "is_available": True
    },

    #HERBS
    {
      "name": "Arugula (Rocket)",
      "description": "Fresh arugula leaves for salads and garnishing.",
      "category": "Herbs",
      "is_available": True
    },
    {
      "name": "Coriander",
      "description": "Fresh coriander for seasoning and garnishing.",
      "category": "Herbs",
      "is_available": True
    },
    {
      "name": "Kale",
      "description": "Fresh kale supplied for salads and cooking.",
      "category": "Herbs",
      "is_available": True
    },
    {
      "name": "Basil",
      "description": "Fresh basil leaves for culinary use.",
      "category": "Herbs",
      "is_available": True
    },
    {
      "name": "Mint",
      "description": "Fresh mint leaves for beverages and garnishing.",
      "category": "Herbs",
      "is_available": True
    },
    {
      "name": "Parsley",
      "description": "Fresh parsley for garnishing and cooking.",
      "category": "Herbs",
      "is_available": True
    },
    {
      "name": "Rocca Leaves",
      "description": "Fresh rocca leaves supplied for salads and culinary use.",
      "category": "Herbs",
      "is_available": True
    },
    {
      "name": "Rosemary",
      "description": "Fresh rosemary for seasoning and flavoring.",
      "category": "Herbs",
      "is_available": True
    },

    #OILS
    {
        "name": "Cold pressed Virgin Coconut Oil",
        "description": "derived from fresh coconut meat without the application of heat or chemicals",
        "category": "Oils",
        "is_available": True
    },
    {
        "name": "Hot pressed Virgin Coconut Oil",
        "description": "carefully produced from quality coconuts using a controlled heat extraction process to deliver a rich, stable oil suitable for everyday use",
        "category": "Oils",
        "is_available": True
    },

    #SPICES
    {
      "name": "Garlic",
      "description": "Fresh garlic bulbs for seasoning and cooking.",
      "category": "Spices",
      "is_available": True
    },
    {
      "name": "Ginger",
      "description": "Fresh garlic bulbs for seasoning and cooking.",
      "category": "Spices",
      "is_available": True
    },
]
        
        
        created = 0
        for product_data in products_data:
            cat_name = product_data.pop('category')

            category_obj = categories.get(cat_name)

            if not category_obj:
                self.stdout.write(self.style.ERROR(f"Skipping{product_data['name']}: Category '{cat_name}' not found in DB"))
                continue

            prod_slug = slugify(product_data["name"])


            product, is_created = Product.objects.get_or_create(
                slug=prod_slug, 
                defaults={
                    **product_data,
                    "category": category_obj,
                    "slug": prod_slug
                }
                #name=product_data["name"],
                #category=category_obj,
                #defaults=product_data
            )

            if is_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f'{product.name}'))
            else:
                 self.stdout.write(self.style.WARNING(f'○ {product.name} exists'))

        self.stdout.write(self.style.SUCCESS(f'\n Created {created} products!'))
        #for product_data in products_data:
            #product, is_created = Product.objects.get_or_create(
               # name=product_data['name'],
           #     defaults=product_data
           #)
           # if is_created:
           #     created += 1
                #else:
                #self.stdout.write(self.style.WARNING(f'○ {product.name}'))

        #self.stdout.write(self.style.SUCCESS(f'\n Created {created} products!'))
