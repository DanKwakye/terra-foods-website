from django.contrib import admin
from django.utils.html import format_html
from .models import Conversation, Message, Appointment, CallbackRequest

# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'visitor_name', 'visitor_email', 'message_count', 'created_at']
    search_fields = ['session_id', 'visitor_name', 'visitor_email']
    readonly_fields = ['session_id', 'created_at', 'updated_at']
    
    def message_count(self, obj):
        count = obj.messages.count()
        return format_html('<strong>{}</strong> messages', count)
    message_count.short_description = 'Messages'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['conversation', 'role', 'content_preview', 'timestamp']
    list_filter = ['role', 'timestamp']
    search_fields = ['content']
    
    def content_preview(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
    content_preview.short_description = 'Content'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'business_type', 'preferred_date', 'preferred_time', 'status', 'created_at']
    list_filter = ['status', 'business_type', 'preferred_date']
    list_editable = ['status']
    search_fields = ['customer_name', 'customer_email', 'customer_phone']
    date_hierarchy = 'preferred_date'
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_name', 'customer_email', 'customer_phone', 'business_type')
        }),
        ('Appointment Details', {
            'fields': ('preferred_date', 'preferred_time', 'notes')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )


@admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_phone', 'preferred_time', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    list_editable = ['status']
    search_fields = ['customer_name', 'customer_phone']
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_name', 'customer_phone')
        }),
        ('Callback Details', {
            'fields': ('preferred_time', 'reason')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )