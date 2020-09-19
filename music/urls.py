from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='music-home'),
    path('about/', views.about,name='music-about'),
]