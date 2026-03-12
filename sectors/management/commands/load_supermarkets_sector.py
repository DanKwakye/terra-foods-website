from django.core.management.base import BaseCommand
from sectors.models import Sector

class Command(BaseCommand):
    help = 'Load Supermarkets sector with complete 7-section content'

    def handle(self, *args, **kwargs):
        
        supermarket, created = Sector.objects.get_or_create(
            slug='supermarket',
            defaults={
                'name': 'Supermarkets',
                'is_active': True,
                'order': 6,
                'meta_description': 'Premium fresh produce supply for supermarkets across Accra. Reliable wholesale delivery, consistent quality, competitive pricing.',
                
                # SECTION 1: Hero
                'hero_h1': 'Fresh Produce for Supermarkets',
                'hero_paragraph_1': 'Terra Foods partners with supermarkets across Accra to deliver consistent, high-quality fresh produce that keeps your shelves stocked and your customers satisfied.',
                'hero_paragraph_2': 'From daily essentials to seasonal specialties, we provide the reliable wholesale supply your supermarket needs to compete and thrive.',
                'hero_paragraph_3': 'Sourced directly from trusted farmers and verified importers, our produce meets the quality standards your customers expect.',
                'hero_cta_text': 'Partner With Us',
                'hero_image': 'https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=1200&h=800&fit=crop',
                
                # SECTION 2: Trust
                'trust_h2': 'Dependable Supply for Retail Success',
                'trust_paragraph': 'Running a successful supermarket requires reliable suppliers who understand the retail environment. Terra Foods delivers on time, every time, with consistent quality and competitive wholesale pricing. We handle the sourcing complexity so you can focus on serving your customers.',
                'trust_cta_text': 'Get Started',
                
                # SECTION 3: Split Left
                'split_left_h2': 'Complete Product Range',
                'split_left_content': '''Terra Foods provides supermarkets with a comprehensive range of fresh produce to meet diverse customer needs.

Our wholesale supply includes fresh vegetables, seasonal fruits, aromatic herbs, quality spices, premium eggs, and specialty oils including virgin coconut oil.

We source both local staples and imported varieties, ensuring your produce section offers the variety and quality that attracts customers and builds loyalty.

From everyday essentials to exotic selections, we deliver the complete range your supermarket needs.''',
                'split_left_cta_text': 'View Product Range',
                'split_left_image': 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=1200&h=800&fit=crop',
                
                # SECTION 4: Split Right
                'split_right_h2': 'Competitive Wholesale Pricing',
                'split_right_content': '''Terra Foods understands the competitive retail landscape and provides wholesale pricing structures designed to protect your margins.

By connecting directly with farmers and managing our own logistics, we eliminate middlemen and pass savings to our supermarket partners.

Our transparent pricing model ensures you get competitive rates without compromising on quality or service.

We work with supermarkets to create customized supply agreements that support your business objectives and profitability goals.''',
                'split_right_cta_text': 'Request Pricing',
                'split_right_image': 'https://images.unsplash.com/photo-1601598851547-4302969d0614?w=1200&h=800&fit=crop',
                
                # SECTION 5: Operations
                'operations_h2': 'Streamlined Wholesale Operations',
                'operations_content': '''**Reliable Delivery Schedules**
We deliver on your schedule with consistent timing that keeps your shelves stocked without overstocking.

**Quality Assurance**
Every delivery is quality-checked to ensure freshness and presentation standards that meet retail expectations.

**Flexible Order Quantities**
Whether you need daily top-ups or bulk weekly deliveries, we scale to your supermarket's requirements.

**Seasonal Planning**
We help you plan for seasonal demand fluctuations with advance notice of availability and pricing.

**Product Variety Management**
Access to both staple items and specialty products lets you differentiate your produce section from competitors.

**Direct Farm Relationships**
Our farmer partnerships ensure consistent supply even during market shortages.''',
                
                # SECTION 6: Partner
                'partner_h2': 'Why Supermarkets Choose Terra Foods',
                'partner_content': '''Supermarkets across Accra partner with Terra Foods because we understand the unique demands of retail fresh produce supply.

**Consistent Quality:** Your customers expect fresh, high-quality produce every time. We deliver consistency that builds trust and repeat business.

**Reliable Supply:** Stock-outs hurt sales and customer loyalty. Our robust supply chain ensures uninterrupted availability.

**Competitive Advantage:** Superior produce quality and variety help differentiate your supermarket in a competitive market.

**Business Support:** We provide more than just products – we partner with you to optimize your produce section performance and profitability.

Let's discuss how Terra Foods can strengthen your supermarket's fresh produce offering.''',
                'partner_cta_text': 'Schedule Consultation',
                'partner_image': 'https://images.unsplash.com/photo-1534723328310-e82dad3ee43f?w=1200&h=800&fit=crop',
                
                # SECTION 7: Dark CTA
                'dark_cta_h2': 'Ready to Elevate Your Produce Section?',
                'dark_cta_paragraph': 'Partner with Terra Foods for reliable wholesale supply, competitive pricing, and the quality your customers demand. Contact us today to discuss a customized supply solution for your supermarket.',
                'dark_cta_button_text': 'Contact Us Now',
                'dark_cta_image': 'https://images.unsplash.com/photo-1583258292688-d0213dc5a3a8?w=1200&h=800&fit=crop',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f' Created Supermarkets sector'))
        else:
            # Update existing
            Sector.objects.filter(slug='supermarkets').update(
                name='Supermarkets',
                is_active=True,
                order=6,
                meta_description='Premium fresh produce supply for supermarkets across Accra. Reliable wholesale delivery, consistent quality, competitive pricing.',
                
                # SECTION 1: Hero
                hero_h1='Fresh Produce for Supermarkets',
                hero_paragraph_1='Terra Foods partners with supermarkets across Accra to deliver consistent, high-quality fresh produce that keeps your shelves stocked and your customers satisfied.',
                hero_paragraph_2='From daily essentials to seasonal specialties, we provide the reliable wholesale supply your supermarket needs to compete and thrive.',
                hero_paragraph_3='Sourced directly from trusted farmers and verified importers, our produce meets the quality standards your customers expect.',
                hero_cta_text='Partner With Us',
                hero_image='https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=1200&h=800&fit=crop',
                
                # SECTION 2: Trust
                trust_h2='Dependable Supply for Retail Success',
                trust_paragraph='Running a successful supermarket requires reliable suppliers who understand the retail environment. Terra Foods delivers on time, every time, with consistent quality and competitive wholesale pricing. We handle the sourcing complexity so you can focus on serving your customers.',
                trust_cta_text='Get Started',
                
                # SECTION 3: Split Left
                split_left_h2='Complete Product Range',
                split_left_content='''Terra Foods provides supermarkets with a comprehensive range of fresh produce to meet diverse customer needs.

Our wholesale supply includes fresh vegetables, seasonal fruits, aromatic herbs, quality spices, premium eggs, and specialty oils including virgin coconut oil.

We source both local staples and imported varieties, ensuring your produce section offers the variety and quality that attracts customers and builds loyalty.

From everyday essentials to exotic selections, we deliver the complete range your supermarket needs.''',
                split_left_cta_text='View Product Range',
                split_left_image='https://images.unsplash.com/photo-1542838132-92c53300491e?w=1200&h=800&fit=crop',
                
                # SECTION 4: Split Right
                split_right_h2='Competitive Wholesale Pricing',
                split_right_content='''Terra Foods understands the competitive retail landscape and provides wholesale pricing structures designed to protect your margins.

By connecting directly with farmers and managing our own logistics, we eliminate middlemen and pass savings to our supermarket partners.

Our transparent pricing model ensures you get competitive rates without compromising on quality or service.

We work with supermarkets to create customized supply agreements that support your business objectives and profitability goals.''',
                split_right_cta_text='Request Pricing',
                split_right_image='https://images.unsplash.com/photo-1601598851547-4302969d0614?w=1200&h=800&fit=crop',
                
                # SECTION 5: Operations
                operations_h2='Streamlined Wholesale Operations',
                operations_content='''**Reliable Delivery Schedules**
We deliver on your schedule with consistent timing that keeps your shelves stocked without overstocking.

**Quality Assurance**
Every delivery is quality-checked to ensure freshness and presentation standards that meet retail expectations.

**Flexible Order Quantities**
Whether you need daily top-ups or bulk weekly deliveries, we scale to your supermarket's requirements.

**Seasonal Planning**
We help you plan for seasonal demand fluctuations with advance notice of availability and pricing.

**Product Variety Management**
Access to both staple items and specialty products lets you differentiate your produce section from competitors.

**Direct Farm Relationships**
Our farmer partnerships ensure consistent supply even during market shortages.''',
                
                # SECTION 6: Partner
                partner_h2='Why Supermarkets Choose Terra Foods',
                partner_content='''Supermarkets across Accra partner with Terra Foods because we understand the unique demands of retail fresh produce supply.

**Consistent Quality:** Your customers expect fresh, high-quality produce every time. We deliver consistency that builds trust and repeat business.

**Reliable Supply:** Stock-outs hurt sales and customer loyalty. Our robust supply chain ensures uninterrupted availability.

**Competitive Advantage:** Superior produce quality and variety help differentiate your supermarket in a competitive market.

**Business Support:** We provide more than just products  we partner with you to optimize your produce section performance and profitability.

Let's discuss how Terra Foods can strengthen your supermarket's fresh produce offering.''',
                partner_cta_text='Schedule Consultation',
                partner_image='https://images.unsplash.com/photo-1534723328310-e82dad3ee43f?w=1200&h=800&fit=crop',
                
                # SECTION 7: Dark CTA
                dark_cta_h2='Ready to Elevate Your Produce Section?',
                dark_cta_paragraph='Partner with Terra Foods for reliable wholesale supply, competitive pricing, and the quality your customers demand. Contact us today to discuss a customized supply solution for your supermarket.',
                dark_cta_button_text='Contact Us Now',
                dark_cta_image='https://images.unsplash.com/photo-1583258292688-d0213dc5a3a8?w=1200&h=800&fit=crop',
            )
            self.stdout.write(self.style.SUCCESS(f' Updated Supermarkets sector'))
        
        self.stdout.write(self.style.SUCCESS('\n🎉 Supermarkets sector loaded successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Visit: /sectors/supermarkets/'))