from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'music/home.html', context)


def about(request):
    return render(request, 'music/about.html', {'title': 'About'})