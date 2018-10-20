from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'faultquakes/home.html', context)


def about(request):
    return render(request, 'faultquakes/about.html', {'title': 'About'})

# Create your views here.

