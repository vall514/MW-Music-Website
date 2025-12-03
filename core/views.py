from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import SiteSettings, Testimonial, ContactMessage, NewsletterSubscriber
from .forms import ContactForm, NewsletterForm
from music.models import Album
from events.models import Event
from blog.models import BlogPost

def home(request):
    latest_album = Album.objects.filter(featured=True).first()
    upcoming_events = Event.objects.filter(is_past=False, is_featured=True)[:3]
    testimonials = Testimonial.objects.filter(featured=True)[:3]
    
    context = {
        'latest_album': latest_album,
        'upcoming_events': upcoming_events,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)

def about(request):
    testimonials = Testimonial.objects.all()[:6]
    context = {'testimonials': testimonials}
    return render(request, 'core/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'core/contact.html', context)

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully subscribed to newsletter!')
        else:
            messages.error(request, 'This email is already subscribed.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))