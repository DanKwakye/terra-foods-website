from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
from datetime import datetime, timedelta
from .models import Conversation, Message, Appointment, CallbackRequest

# Import OpenAI with new client
try:
    from openai import OpenAI
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    OPENAI_AVAILABLE = True
except Exception as e:
    print(f"OpenAI initialization error: {e}")
    OPENAI_AVAILABLE = False

# Yaa's personality and context with FAQs
SYSTEM_PROMPT = """You are Yaa, a friendly and professional female AI assistant for Terra Foods, a premium fresh organic produce supplier in Accra, Ghana.

ABOUT TERRA FOODS:
- We deliver fresh organic vegetables, fruits, herbs, spices, eggs, and premium oils (virgin coconut oil) throughout Accra
- We serve hotels, restaurants, executive chefs, event catering, corporate offices, and supermarkets
- Key features: Fresh from farm, lightning-fast delivery, quality guarantee, wide selection
- Contact: WhatsApp/Phone: +233 54 446 8232, Email: info@terrafoodsgh.com
- Sourcing: Direct from trusted local farmers and verified suppliers/importers

FREQUENTLY ASKED QUESTIONS & ANSWERS:

1. What products does Terra Foods supply?
Terra Foods supplies a wide range of fresh produce including vegetables, fruits, herbs, spices, eggs, and premium oils such as virgin coconut oil. We source products directly from trusted farmers and suppliers to ensure quality and freshness.

2. Who do you supply?
We supply businesses such as hotels, restaurants, executive chefs, event caterers, corporate kitchens, and supermarkets across Accra.

3. Where do you source your produce?
Our produce is sourced directly from trusted local farmers and verified suppliers. For products that are not locally available, we partner with reliable importers to ensure our clients receive everything they need.

4. Do you offer delivery services?
Yes. Terra Foods provides reliable delivery services across Accra to ensure fresh produce reaches your kitchen or business quickly and efficiently.

5. Can businesses order in bulk?
Absolutely. Terra Foods is structured to handle both small and large orders, making it easy for restaurants, hotels, caterers, and supermarkets to procure produce in the quantities they require.

6. How do I place an order?
Orders can be placed through our website, via WhatsApp, or by contacting our team directly. Our team will assist you with product selection, pricing, and delivery arrangements.

7. Can you source products not listed on the website?
Yes. If there is a specific product you need that is not listed on our website, we can source it for you through our network of farmers and suppliers.

8. How do you ensure the freshness of your produce?
We work closely with farmers and suppliers to source produce at the right time and deliver it promptly. Our logistics process ensures products reach your business as fresh as possible.

9. Do you work with long-term supply partnerships?
Yes. Terra Foods is built to support long-term supply partnerships with businesses that require consistent, reliable access to fresh produce.

10. Why should businesses choose Terra Foods?
Terra Foods simplifies procurement by connecting farmers and suppliers directly to businesses. Our focus on quality sourcing, reliable supply, and efficient delivery ensures that kitchens and businesses receive fresh ingredients consistently without the stress of traditional market sourcing.

11. How does Terra Foods support farmers?
Terra Foods helps farmers access reliable markets by connecting their produce directly with businesses. This helps reduce food waste, improve farmer income, and strengthen the agricultural supply chain.

YOUR CAPABILITIES:
1. Answer questions about Terra Foods, products, and services using the FAQs above
2. Book appointments for business consultations
3. Schedule callback requests
4. Provide product information
5. Explain our services for different sectors (hotels, restaurants, etc.)
6. Help with order inquiries

YOUR PERSONALITY:
- Warm, friendly, and professional Ghanaian female assistant
- Helpful and proactive
- Use a conversational, natural tone
- Keep responses concise but informative (2-4 sentences max unless explaining complex topics)
- Show enthusiasm for fresh produce and helping customers
- Use welcoming phrases like "Hello!" "How can I help you today?" "I'm happy to assist!"

CONVERSATION GUIDELINES:
- Greet visitors warmly on first contact
- If someone asks about products, pricing, or specific orders, provide info and suggest they contact the team via WhatsApp or phone for details
- If someone wants to book an appointment, tell them you can help with that
- If someone wants a callback, tell them you can schedule that
- Always be helpful and redirect to human team for complex negotiations or pricing

Respond naturally, warmly, and professionally!"""


@csrf_exempt
def chat(request):
    """
    Advanced AI chat endpoint with OpenAI integration
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            session_id = data.get('session_id', 'default')
            action = data.get('action', '')
            
            # Get or create conversation
            conversation, created = Conversation.objects.get_or_create(session_id=session_id)
            
            # Handle special actions
            if action == 'book_appointment':
                return handle_appointment_booking(request, conversation, data)
            elif action == 'request_callback':
                return handle_callback_request(request, conversation, data)
            
            # Save user message
            Message.objects.create(
                conversation=conversation,
                role='user',
                content=message
            )
            
            # Get conversation history
            history = get_conversation_history(conversation)
            
            # Get AI response
            if OPENAI_AVAILABLE and settings.OPENAI_API_KEY:
                response = get_ai_response(history, message)
            else:
                response = get_fallback_response(message)
            
            # Save assistant message
            Message.objects.create(
                conversation=conversation,
                role='assistant',
                content=response
            )
            
            # Detect if booking intent
            booking_intent = detect_booking_intent(response)
            
            return JsonResponse({
                'response': response,
                'session_id': session_id,
                'booking_intent': booking_intent
            })
            
        except Exception as e:
            print(f"Chat error: {e}")
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'POST method required'}, status=400)


def get_conversation_history(conversation, limit=10):
    """Get recent conversation history"""
    messages = conversation.messages.all().order_by('-timestamp')[:limit]
    history = []
    for msg in reversed(messages):
        history.append({
            'role': msg.role,
            'content': msg.content
        })
    return history


def get_ai_response(history, new_message):
    """Get response from OpenAI using new client format"""
    try:
        messages = [{'role': 'system', 'content': SYSTEM_PROMPT}]
        
        # Add conversation history
        for msg in history[-5:]:  # Last 5 messages only
            messages.append({
                'role': msg['role'],
                'content': msg['content']
            })
        
        # Add new message
        messages.append({
            'role': 'user',
            'content': new_message
        })
        
        # Call OpenAI with new client
        response = client.chat.completions.create(
            model='gpt-3.5-turbo',  # Using cheaper model
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return get_fallback_response(new_message)


def get_fallback_response(message):
    """Fallback responses when OpenAI is not available"""
    message_lower = message.lower()
    
    # Product questions
    if any(word in message_lower for word in ['product', 'supply', 'sell', 'offer', 'have']):
        return "Terra Foods supplies a wide range of fresh produce including vegetables, fruits, herbs, spices, eggs, and premium oils such as virgin coconut oil. We source products directly from trusted farmers and suppliers to ensure quality and freshness. 🌿<br><br>Would you like to know more about a specific category?"
    
    # Who we supply
    elif any(word in message_lower for word in ['who', 'customer', 'client', 'serve']):
        return "We supply businesses such as hotels, restaurants, executive chefs, event caterers, corporate kitchens, and supermarkets across Accra. 🏨🍽️<br><br>Which sector are you in?"
    
    # Delivery
    elif any(word in message_lower for word in ['deliver', 'delivery', 'ship']):
        return "Yes! Terra Foods provides reliable delivery services across Accra to ensure fresh produce reaches your kitchen or business quickly and efficiently. 🚚<br><br>What area are you located in?"
    
    # Ordering
    elif any(word in message_lower for word in ['order', 'buy', 'purchase', 'how to']):
        return "Orders can be placed through our website, via WhatsApp, or by contacting our team directly. Our team will assist you with product selection, pricing, and delivery arrangements.<br><br>Would you like me to connect you with our team?"
    
    # Bulk orders
    elif any(word in message_lower for word in ['bulk', 'large', 'quantity', 'wholesale']):
        return "Absolutely! Terra Foods is structured to handle both small and large orders, making it easy for restaurants, hotels, caterers, and supermarkets to procure produce in the quantities they require. 📦<br><br>What quantities are you looking for?"
    
    # Freshness
    elif any(word in message_lower for word in ['fresh', 'quality', 'how fresh']):
        return "We work closely with farmers and suppliers to source produce at the right time and deliver it promptly. Our logistics process ensures products reach your business as fresh as possible. ✨<br><br>Quality is our top priority!"
    
    # Appointment
    elif any(word in message_lower for word in ['appointment', 'meeting', 'visit', 'book']):
        return "I'd be happy to help you book an appointment with our team! We can schedule a consultation to discuss your specific needs.<br><br>Would you like to book an appointment now?"
    
    # Callback
    elif any(word in message_lower for word in ['call', 'callback', 'phone', 'call me']):
        return "I can schedule a callback for you! Our team would be happy to call you at your convenience.<br><br>Would you like to request a callback?"
    
    # Greeting
    elif any(word in message_lower for word in ['hello', 'hi', 'hey', 'good morning', 'good afternoon']):
        return "Hello! 👋 I'm Yaa, your Terra Foods assistant. How can I help you today?<br><br>I can answer questions about our products, services, delivery, or help you book an appointment!"
    
    # Thank you
    elif any(word in message_lower for word in ['thank', 'thanks']):
        return "You're very welcome! 😊 Is there anything else I can help you with?<br><br>Feel free to reach out anytime via WhatsApp at +233 54 446 8232!"
    
    # Default
    else:
        return "I'd be happy to help! For detailed information about that, please contact our team directly via WhatsApp at +233 54 446 8232 or call us.<br><br>Alternatively, I can help you with:<br>• Product information<br>• Delivery details<br>• Booking an appointment<br>• Requesting a callback<br><br>What would you like to know?"


def detect_booking_intent(response):
    """Detect if AI is trying to book appointment or callback"""
    booking_keywords = ['book', 'appointment', 'schedule', 'meeting', 'visit']
    callback_keywords = ['call you', 'callback', 'call back', 'phone you']
    
    response_lower = response.lower()
    
    if any(keyword in response_lower for keyword in booking_keywords):
        return 'appointment'
    elif any(keyword in response_lower for keyword in callback_keywords):
        return 'callback'
    
    return None


def handle_appointment_booking(request, conversation, data):
    """Handle appointment booking"""
    try:
        appointment_data = data.get('appointment_data', {})
        
        appointment = Appointment.objects.create(
            conversation=conversation,
            customer_name=appointment_data.get('name'),
            customer_email=appointment_data.get('email'),
            customer_phone=appointment_data.get('phone'),
            business_type=appointment_data.get('business_type'),
            preferred_date=appointment_data.get('date'),
            preferred_time=appointment_data.get('time'),
            notes=appointment_data.get('notes', '')
        )
        
        response = f"Perfect! I've scheduled your appointment for {appointment.preferred_date} at {appointment.preferred_time}.<br><br>Our team will contact you at {appointment.customer_phone} to confirm the details.<br><br>Thank you for choosing Terra Foods!"
        
        # Save to conversation
        Message.objects.create(
            conversation=conversation,
            role='assistant',
            content=response
        )
        
        return JsonResponse({
            'response': response,
            'success': True,
            'appointment_id': appointment.id
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def handle_callback_request(request, conversation, data):
    """Handle callback request"""
    try:
        callback_data = data.get('callback_data', {})
        
        callback = CallbackRequest.objects.create(
            conversation=conversation,
            customer_name=callback_data.get('name'),
            customer_phone=callback_data.get('phone'),
            preferred_time=callback_data.get('time'),
            reason=callback_data.get('reason', '')
        )
        
        response = f"Great! I've scheduled a callback for {callback.preferred_time}.<br><br>We'll call you at {callback.customer_phone}.<br><br>Looking forward to speaking with you!"
        
        # Save to conversation
        Message.objects.create(
            conversation=conversation,
            role='assistant',
            content=response
        )
        
        return JsonResponse({
            'response': response,
            'success': True,
            'callback_id': callback.id
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)