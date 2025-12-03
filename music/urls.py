from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.music_list, name='list'),
    path('<int:pk>/', views.album_detail, name='detail'),
]