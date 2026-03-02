from django.core.management.base import BaseCommand
from sectors.models import Sector

class Command(BaseCommand):
    help = 'Load complete 7-section sectors'

    def handle(self, *args, **kwargs):
        sectors_data = [
            # ==================== HOTELS ====================
            {
                'name': 'Hotels',
                'hero_h1': 'Premium Fresh Produce Supply for Hotels in Accra',
                'hero_paragraph_1': 'We understand the demands of hotel kitchens. Consistent quality, reliable delivery, and impeccable freshness aren\'t just expectations—they\'re requirements.',
                'hero_paragraph_2': 'Terra Foods provides Accra\'s leading hotels with farm-fresh organic produce, delivered daily to your specifications. From executive breakfast buffets to fine dining establishments, we ensure your kitchen never compromises on quality.',
                'hero_paragraph_3': 'Our dedicated hotel supply team works directly with your procurement and culinary teams, providing personalized service that adapts to your property\'s unique needs and schedules.',
                'hero_cta_text': 'Request Supply Quote',
                'trust_h2': 'Reliable Fresh Produce Delivery for Accra\'s Leading Hotels',
                'trust_paragraph': 'Sourced from carefully vetted local farms. Early morning delivery windows that work with your kitchen schedules. Temperature-controlled transportation to maintain peak freshness. Consistent stock availability—even during seasonal transitions. Our hotel supply program is built on reliability you can count on, day after day.',
                'trust_cta_text': 'Speak to Our Supply Team',
                'split_left_h2': 'Seasonal Produce for Premium Hotel Kitchens',
                'split_left_content': 'We work directly with local farms across Ghana to bring you seasonal produce at peak quality. Our quality control process ensures every delivery meets hotel-grade standards.\n\nDaily freshness checks and rapid farm-to-kitchen delivery mean your guests enjoy produce at its absolute best. We understand seasonality and help you plan menus around optimal availability.',
                'split_left_cta_text': 'View Seasonal Guide',
                'split_right_h2': 'Reduce Kitchen Prep Time',
                'split_right_content': 'Pre-cut vegetables and fruits prepared to your specifications. Bulk supply options that reduce ordering frequency. Custom orders for special events and menu changes.\n\nOur prep services save your kitchen team hours of labor while maintaining the freshness and quality your guests expect. Focus on cooking excellence while we handle the preparation.',
                'split_right_cta_text': 'Explore Prep Options',
                'operations_h2': 'Built for Hotel Operations',
                'operations_content': 'Scheduled delivery windows that align with your kitchen operations. Inventory forecasting to prevent stockouts during peak seasons. Emergency supply access for unexpected events or menu changes.\n\nDedicated account manager who understands your property\'s needs. Flexible ordering through WhatsApp, phone, or email. Volume pricing that improves your bottom line without compromising quality.',
                'partner_h2': 'Partner with Terra Foods',
                'partner_content': 'Join Accra\'s leading hotels who trust Terra Foods for their daily produce needs. We\'re more than a supplier—we\'re a partner invested in your culinary success.\n\nOur hotel partnership program provides preferential pricing, priority delivery, and dedicated support. Let\'s discuss how we can elevate your hotel\'s food service together.',
                'partner_cta_text': 'Become a Partner',
                'dark_cta_h2': 'Ready to Elevate Your Hotel Kitchen?',
                'dark_cta_paragraph': 'We supply Accra\'s leading hotels with premium organic produce, delivering excellence your guests can taste. Let\'s start a conversation about your hotel\'s needs.',
                'dark_cta_button_text': 'Request Quote',
                'order': 1,
            },
            
            # ==================== RESTAURANTS ====================
            {
                'name': 'Restaurants',
                'hero_h1': 'Restaurant-Grade Fresh Produce Delivered Daily in Accra',
                'hero_paragraph_1': 'Your menu reputation depends on ingredient quality. Whether you\'re running a fine dining establishment or a neighborhood favorite, Terra Foods ensures your kitchen always has the freshest produce.',
                'hero_paragraph_2': 'We supply restaurants across Accra with organic, farm-fresh ingredients that meet professional kitchen standards. Flexible delivery schedules, consistent quality, and responsive service designed specifically for restaurant operations.',
                'hero_paragraph_3': 'Our restaurant supply program understands the unique pressures of food service—tight margins, demanding customers, and the need for absolute reliability.',
                'hero_cta_text': 'Get Restaurant Pricing',
                'trust_h2': 'Reliable Fresh Produce Delivery for Accra\'s Best Restaurants',
                'trust_paragraph': 'Early morning deliveries before service begins. Locally sourced ingredients that support Ghana\'s farming community. Temperature-controlled transport maintains freshness. Consistent availability of your menu staples. Our restaurant supply program is built around the realities of professional kitchens.',
                'trust_cta_text': 'Talk to a Supply Specialist',
                'split_left_h2': 'Quality That Enhances Your Menu',
                'split_left_content': 'Every chef knows: great dishes start with great ingredients. We source directly from vetted local farms, ensuring restaurant-grade quality in every delivery.\n\nOur quality standards match professional kitchen expectations. From crisp vegetables to perfectly ripe fruits, we deliver produce your customers will notice.',
                'split_left_cta_text': 'See Quality Standards',
                'split_right_h2': 'Streamline Your Kitchen Operations',
                'split_right_content': 'Predictable delivery windows that work with your prep schedule. Bulk ordering options that reduce costs. Custom cuts and preparations available.\n\nOur restaurant program is designed to make your operations smoother, letting your team focus on what they do best—creating memorable dining experiences.',
                'split_right_cta_text': 'Learn About Services',
                'operations_h2': 'Built for Restaurant Kitchens',
                'operations_content': 'Scheduled deliveries that don\'t disrupt service. Emergency orders when you need them. Seasonal menu planning support from our team.\n\nDedicated restaurant account manager. Volume pricing that improves your food cost. Flexible payment terms for established partners.',
                'partner_h2': 'Join Accra\'s Top Restaurant Kitchens',
                'partner_content': 'Partner with the supplier that understands restaurant operations. We work with Accra\'s finest dining establishments, casual restaurants, and everything in between.\n\nOur restaurant partnership program provides competitive pricing, priority service, and support that grows with your business.',
                'partner_cta_text': 'Start Your Partnership',
                'dark_cta_h2': 'Ready to Enhance Your Restaurant Kitchen?',
                'dark_cta_paragraph': 'Join the restaurants across Accra that rely on Terra Foods for premium fresh produce. Let\'s discuss your kitchen\'s specific needs.',
                'dark_cta_button_text': 'Request Quote',
                'order': 2,
            },
            
            # ==================== EXECUTIVE CHEFS ====================
            {
                'name': 'Executive Chefs',
                'hero_h1': 'Premium Produce for Executive Chefs in Accra',
                'hero_paragraph_1': 'As an executive chef, you demand perfection. Every ingredient must meet your exacting standards, arrive on time, and perform consistently in your kitchen.',
                'hero_paragraph_2': 'Terra Foods works directly with executive chefs across Accra, providing hand-selected organic produce that meets professional culinary standards. We understand your vision and source ingredients worthy of it.',
                'hero_paragraph_3': 'Our executive chef program provides direct access to our procurement team, allowing you to specify exactly what you need, when you need it.',
                'hero_cta_text': 'Schedule Chef Consultation',
                'trust_h2': 'Trusted by Accra\'s Leading Executive Chefs',
                'trust_paragraph': 'Hand-selected produce chosen to your specifications. Direct line to our sourcing team for special requests. Seasonal availability planning for menu development. Consistent quality across all deliveries. We understand the standards executive chefs require and deliver accordingly.',
                'trust_cta_text': 'Speak with Our Team',
                'split_left_h2': 'Sourced for Culinary Excellence',
                'split_left_content': 'We work with you to understand your culinary vision and source ingredients that bring it to life. Quality markers, seasonality, and consistency are our priorities.\n\nOur team personally inspects produce to ensure it meets professional kitchen standards. We understand what executive chefs look for and deliver it.',
                'split_left_cta_text': 'View Sourcing Process',
                'split_right_h2': 'Specialized Ingredient Sourcing',
                'split_right_content': 'Need something specific? We source unique ingredients upon request. Specialty herbs, heirloom vegetables, or seasonal items—if it grows in Ghana, we can get it.\n\nOur network of local farmers and suppliers means we can fulfill special requests that typical suppliers cannot.',
                'split_right_cta_text': 'Request Specialty Items',
                'operations_h2': 'Built for Professional Kitchens',
                'operations_content': 'Flexible delivery scheduling around your kitchen operations. Direct communication with our procurement team. Priority access to limited seasonal items.\n\nPersonalized service that understands the demands of executive-level culinary operations. We adapt to your needs, not the other way around.',
                'partner_h2': 'Partner with Terra Foods',
                'partner_content': 'Join executive chefs across Accra who trust Terra Foods for premium ingredients. We\'re more than a supplier—we\'re a partner in your culinary success.\n\nOur executive chef partnership provides preferential access, custom sourcing, and dedicated support.',
                'partner_cta_text': 'Start Partnership',
                'dark_cta_h2': 'Ready to Elevate Your Culinary Vision?',
                'dark_cta_paragraph': 'We supply Accra\'s leading executive chefs with hand-selected premium produce. Let\'s discuss your kitchen\'s specific requirements.',
                'dark_cta_button_text': 'Get Started',
                'order': 3,
            },
            
            # ==================== EVENT CATERING ====================
            {
                'name': 'Event Catering',
                'hero_h1': 'Fresh Produce for Event Catering in Accra',
                'hero_paragraph_1': 'Event catering demands precision. Large volumes, specific timing, and zero room for error. Terra Foods specializes in delivering exactly what you need, exactly when you need it.',
                'hero_paragraph_2': 'From intimate gatherings to large-scale events serving hundreds, we provide fresh organic produce with the reliability event catering requires.',
                'hero_paragraph_3': 'Our event catering program includes advanced ordering, guaranteed availability, and delivery timed to your preparation schedule.',
                'hero_cta_text': 'Plan Event Supply',
                'trust_h2': 'Reliable Fresh Produce for Event Success',
                'trust_paragraph': 'Large-volume orders without compromising quality. Guaranteed availability through advance ordering. Delivery scheduled to match your prep timeline. Volume pricing that improves your margins. Our event catering program handles the logistics so you can focus on execution.',
                'trust_cta_text': 'Discuss Your Event',
                'split_left_h2': 'Volume Supply Without Compromise',
                'split_left_content': 'Whether you\'re catering for 50 or 500, we ensure consistent quality across your entire order. Our volume supply capability doesn\'t sacrifice freshness.\n\nAdvanced planning with our team ensures availability even during peak event seasons. We work with you to forecast quantities and prevent shortages.',
                'split_left_cta_text': 'See Volume Pricing',
                'split_right_h2': 'Precision Timing for Event Success',
                'split_right_content': 'Event timing is everything. We deliver on your schedule, not ours. Early morning deliveries, day-before staging, or same-day service—we adapt to your event needs.\n\nOur logistics team coordinates with your catering schedule to ensure seamless delivery that doesn\'t disrupt your preparation.',
                'split_right_cta_text': 'Schedule Delivery',
                'operations_h2': 'Built for Event Catering',
                'operations_content': 'Advanced ordering for guaranteed availability. Flexible delivery scheduling around your event prep. Emergency supply access for last-minute changes.\n\nDedicated event catering coordinator. Custom quantities and cuts available. Post-event ordering support for recurring clients.',
                'partner_h2': 'Partner with Terra Foods',
                'partner_content': 'Join event caterers across Accra who rely on Terra Foods for reliable supply. We understand the pressures of event catering and deliver accordingly.\n\nOur event catering partnership provides priority scheduling, volume discounts, and dedicated support.',
                'partner_cta_text': 'Become a Partner',
                'dark_cta_h2': 'Ready to Simplify Event Catering?',
                'dark_cta_paragraph': 'We supply event caterers across Accra with reliable, high-quality produce. Let\'s discuss your upcoming event requirements.',
                'dark_cta_button_text': 'Plan Your Event',
                'order': 4,
            },
            
            # ==================== CORPORATE ====================
            {
                'name': 'Corporate',
                'hero_h1': 'Fresh Produce for Corporate Offices in Accra',
                'hero_paragraph_1': 'Keep your team healthy and productive with fresh organic produce delivered directly to your office. Terra Foods supplies corporate cafeterias, executive lounges, and staff kitchens across Accra.',
                'hero_paragraph_2': 'Our corporate supply program provides regular deliveries of fresh fruits, vegetables, and healthy snacks that support employee wellness and workplace satisfaction.',
                'hero_paragraph_3': 'Flexible ordering, corporate invoicing, and dedicated account management designed specifically for business procurement processes.',
                'hero_cta_text': 'Set Up Corporate Account',
                'trust_h2': 'Reliable Fresh Produce for Corporate Wellness',
                'trust_paragraph': 'Regular scheduled deliveries around your office hours. Fresh healthy options for your team. Corporate invoicing and payment terms. Flexible ordering for changing headcounts. Our corporate program is designed around business operations.',
                'trust_cta_text': 'Contact Corporate Team',
                'split_left_h2': 'Support Employee Wellness',
                'split_left_content': 'Healthy employees are productive employees. Provide your team with fresh organic produce that supports wellness and shows you value their health.\n\nFrom executive lounges to staff cafeterias, we supply fresh options that improve workplace satisfaction and productivity.',
                'split_left_cta_text': 'View Wellness Options',
                'split_right_h2': 'Flexible Corporate Ordering',
                'split_right_content': 'Headcount changes? Menu adjustments? Last-minute meetings? Our corporate program adapts to your business needs with flexible ordering and responsive service.\n\nCustom orders for special dietary requirements or preferences. We work with your office management or HR team to ensure smooth operations.',
                'split_right_cta_text': 'Learn About Flexibility',
                'operations_h2': 'Built for Corporate Operations',
                'operations_content': 'Scheduled deliveries around business hours. Corporate invoicing and NET payment terms. Volume pricing that improves your budget.\n\nDedicated corporate account manager. Easy ordering via WhatsApp, email, or phone. Regular service reviews to optimize supply.',
                'partner_h2': 'Partner with Terra Foods',
                'partner_content': 'Join corporations across Accra that prioritize employee wellness with Terra Foods. We understand corporate procurement and deliver accordingly.\n\nOur corporate partnership provides preferential pricing, flexible terms, and dedicated support.',
                'partner_cta_text': 'Start Corporate Account',
                'dark_cta_h2': 'Ready to Enhance Workplace Wellness?',
                'dark_cta_paragraph': 'We supply corporate offices across Accra with fresh healthy produce. Let\'s discuss your workplace wellness program.',
                'dark_cta_button_text': 'Contact Us',
                'order': 5,
            },
        ]
        
        created = 0
        updated = 0
        for sector_data in sectors_data:
            sector, is_created = Sector.objects.get_or_create(
                name=sector_data['name'],
                defaults=sector_data
            )
            if is_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Created: {sector.name}'))
            else:
                for key, value in sector_data.items():
                    if key != 'name':
                        setattr(sector, key, value)
                sector.save()
                updated += 1
                self.stdout.write(self.style.WARNING(f'○ Updated: {sector.name}'))

        self.stdout.write(self.style.SUCCESS(f'\n✅ Created {created} new sectors, updated {updated} existing!'))