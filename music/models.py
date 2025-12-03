from django.db import models
from ckeditor.fields import RichTextField

class Album(models.Model):
    ALBUM_TYPES = [
        ('album', 'Album'),
        ('ep', 'EP'),
        ('single', 'Single'),
    ]
    
    title = models.CharField(max_length=200)
    album_type = models.CharField(max_length=10, choices=ALBUM_TYPES)
    release_date = models.DateField()
    cover_art = models.ImageField(upload_to='albums/')
    description = RichTextField()
    spotify_url = models.URLField(blank=True)
    apple_music_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    soundcloud_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-release_date']
    
    def __str__(self):
        return f"{self.title} ({self.album_type})"

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=200)
    track_number = models.IntegerField()
    duration = models.CharField(max_length=10, help_text="Format: MM:SS")
    lyrics = RichTextField(blank=True)
    story_behind = RichTextField(blank=True, help_text="Story behind the song")
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)
    
    class Meta:
        ordering = ['album', 'track_number']
    
    def __str__(self):
        return f"{self.album.title} - {self.track_number}. {self.title}"