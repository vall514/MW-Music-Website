from django.contrib import admin
from .models import Album, Song

class SongInline(admin.TabularInline):
    model = Song
    extra = 1
    fields = ['track_number', 'title', 'duration']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'album_type', 'release_date', 'featured']
    list_filter = ['album_type', 'featured', 'release_date']
    search_fields = ['title', 'description']
    inlines = [SongInline]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'album', 'track_number', 'duration']
    list_filter = ['album']
    search_fields = ['title', 'lyrics']
