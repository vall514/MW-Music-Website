from django.db import models
from ckeditor.fields import RichTextField

class Event(models.Model):
    EVENT_TYPES = [
        ('concert', 'Concert'),
        ('church', 'Church Service'),
        ('outreach', 'Outreach'),
        ('conference', 'Conference'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    description = RichTextField()
    date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    venue = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Kenya")
    image = models.ImageField(upload_to='events/')
    ticket_url = models.URLField(blank=True, help_text="Link to buy tickets")
    is_featured = models.BooleanField(default=False)
    is_past = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.title} - {self.date.strftime('%Y-%m-%d')}"

class EventGallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='events/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Event Galleries"
    
    def __str__(self):
        return f"{self.event.title} - Image"