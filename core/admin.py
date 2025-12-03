from django.contrib import admin
from .models import SiteSettings, Testimonial, ContactMessage, NewsletterSubscriber

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'email', 'phone']
    
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['name', 'organization', 'text']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message_type', 'subject', 'read', 'created_at']
    list_filter = ['message_type', 'read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'active', 'subscribed_at']
    list_filter = ['active', 'subscribed_at']
    search_fields = ['email']