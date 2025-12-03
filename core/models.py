from django.db import models
from ckeditor.fields import RichTextField

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="MW Music")
    tagline = models.CharField(max_length=200)
    about_short = models.TextField(max_length=500)
    about_full = RichTextField()
    mission_vision = RichTextField()
    logo = models.ImageField(upload_to='site/')
    hero_image = models.ImageField(upload_to='site/')
    hero_video_url = models.URLField(blank=True, null=True)
    
    # Contact info
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    spotify_url = models.URLField(blank=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return self.site_name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.organization}"

class ContactMessage(models.Model):
    MESSAGE_TYPES = [
        ('general', 'General Inquiry'),
        ('booking', 'Booking Request'),
        ('press', 'Press/Media'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email
