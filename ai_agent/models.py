from django.db import models

class Conversation(models.Model):
    """Store AI agent conversations"""
    session_id = models.CharField(max_length=100, unique=True)
    visitor_name = models.CharField(max_length=100, blank=True)
    visitor_email = models.EmailField(blank=True)
    visitor_phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Conversation {self.session_id}"
    
    class Meta:
        ordering = ['-updated_at']


class Message(models.Model):
    """Individual messages in a conversation"""
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=20, choices=[('user', 'User'), ('assistant', 'Assistant')])
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.role}: {self.content[:50]}"
    
    class Meta:
        ordering = ['timestamp']


class Appointment(models.Model):
    """Appointments booked through AI agent"""
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='appointments')
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    business_type = models.CharField(max_length=100, help_text="Hotel, Restaurant, etc.")
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.preferred_date}"
    
    class Meta:
        ordering = ['-created_at']


class CallbackRequest(models.Model):
    """Callback requests scheduled through AI agent"""
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='callbacks')
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    preferred_time = models.CharField(max_length=100, help_text="e.g., 'Morning', 'Afternoon', '2-4 PM'")
    reason = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.preferred_time}"
    
    class Meta:
        ordering = ['-created_at']