from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Conversation, Message

@csrf_exempt
def chat(request):
    """
    AI Agent chat endpoint
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            session_id = data.get('session_id', 'default')
            
            # Get or create conversation
            conversation, created = Conversation.objects.get_or_create(session_id=session_id)
            
            # Save user message
            Message.objects.create(
                conversation=conversation,
                role='user',
                content=message
            )
            
            # Simple AI response (you'll enhance this later with actual AI)
            response = generate_response(message)
            
            # Save assistant message
            Message.objects.create(
                conversation=conversation,
                role='assistant',
                content=response
            )
            
            return JsonResponse({
                'response': response,
                'session_id': session_id
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'POST method required'}, status=400)


def generate_response(message):
    """
    Simple rule-based responses (you can replace with actual AI later)
    """
    message_lower = message.lower()
    
    # Product inquiries
    if 'vegetables' in message_lower or 'veggies' in message_lower:
        return "We have a wide selection of fresh organic vegetables including spinach, tomatoes, carrots, cabbage and more. Would you like to know about specific vegetables or place an order?"
    
    elif 'fruits' in message_lower or 'fruit' in message_lower:
        return "Our fruit selection includes bananas, pineapples, oranges, watermelon, papaya and more. All organic and farm-fresh. What fruits are you interested in?"
    
    elif 'herbs' in message_lower or 'herb' in message_lower:
        return "We offer fresh herbs including mint, parsley, basil, and rosemary. Perfect for cooking and garnishing. Need specific herbs?"
    
    elif 'spices' in message_lower or 'spice' in message_lower:
        return "We have fresh spices like ginger, garlic, onions, and peppers. All organic. What spices do you need?"
    
    elif 'oils' in message_lower or 'oil' in message_lower:
        return "We stock pure virgin oils including coconut oil and extra virgin olive oil. Both are cold-pressed and organic. Interested in ordering?"
    
    # Ordering
    elif 'order' in message_lower or 'buy' in message_lower:
        return "Great! You can place an order via WhatsApp at +233 XXX XXX XXX or call us directly. We deliver throughout Accra with lightning-fast service. What would you like to order?"
    
    # Delivery
    elif 'delivery' in message_lower or 'deliver' in message_lower:
        return "We deliver throughout Accra with same-day delivery available for orders placed before 2pm. Delivery is fast and reliable. Where would you like your order delivered?"
    
    # Pricing
    elif 'price' in message_lower or 'cost' in message_lower or 'how much' in message_lower:
        return "For current pricing and availability, please contact us via WhatsApp at +233 XXX XXX XXX or call us. We'll be happy to provide a quote based on your specific needs."
    
    # Business sectors
    elif 'hotel' in message_lower or 'restaurant' in message_lower or 'corporate' in message_lower or 'catering' in message_lower:
        return "We supply fresh produce to hotels, restaurants, corporate offices, and catering services across Accra. We offer volume discounts and flexible delivery schedules. Would you like to discuss your business requirements?"
    
    # Contact
    elif 'contact' in message_lower or 'reach' in message_lower or 'phone' in message_lower:
        return "You can reach us via:\n- WhatsApp: +233 XXX XXX XXX\n- Phone: +233 XXX XXX XXX\n- Email: info@terrafoods.com\nWe're here to help!"
    
    # Default response
    else:
        return "Hi! I'm here to help you with fresh organic produce. You can ask me about our products (vegetables, fruits, herbs, spices, oils), delivery, ordering, or business supplies. How can I assist you today?"

# Create your views here.
