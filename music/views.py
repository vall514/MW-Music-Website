from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def music_list(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'music/music_list.html', context)

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    context = {'album': album}
    return render(request, 'music/album_detail.html', context)