from django.db import models

# Create your models here.
class Conversation(models.Model):
    """
     Store AI agent conversations
    """
    session_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation {self.session_id}"
    
    class Meta:
        ordering = ['-updated_at']

class Message(models.Model):
    """
    Individual messages in a conversation
    """
    Conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=20, choices=[('user', 'User'), ('assistant', 'Assistant')])
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.role}: {self.content[:50]}"
    

    class Meta:
        ordering = ['timestamp']