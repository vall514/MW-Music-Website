from django.contrib import admin
from .models import Event, EventGallery

class EventGalleryInline(admin.TabularInline):
    model = EventGallery
    extra = 3

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'date', 'venue', 'city', 'is_featured', 'is_past']
    list_filter = ['event_type', 'is_featured', 'is_past', 'date']
    search_fields = ['title', 'venue', 'city']
    inlines = [EventGalleryInline]