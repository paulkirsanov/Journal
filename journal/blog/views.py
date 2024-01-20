from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import BlogForm


def index(request):
    posts = BlogForm.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница',
    }
    return render(request, 'blog/index.html', context)


def about(request):
    bl = BlogForm()
    context = {'form': bl, 'title': 'About'}
    return render(request, 'blog/about.html', context)


def show_post(request, post_id):
    post = get_object_or_404(BlogForm, pk=post_id)

    context = {
        'post': post,
        'title': post.title,
    }
    return render(request, 'blog/themes.html', context=context)
