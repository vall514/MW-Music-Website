from django.shortcuts import render, get_object_or_404
from .models import Event

def events_list(request):
    upcoming_events = Event.objects.filter(is_past=False)
    past_events = Event.objects.filter(is_past=True)[:6]
    
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    return render(request, 'events/events_list.html', context)

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {'event': event}
    return render(request, 'events/event_detail.html', context)