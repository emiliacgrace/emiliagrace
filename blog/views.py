from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def home(request):
    posts = BlogPost.objects.order_by('-published_date')
    return render(request, 'home.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})
