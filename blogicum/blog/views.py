"""Представления приложения blog."""
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def get_published_posts():
    """Возвращает запрос с опубликованными постами."""
    return Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    """Отображает главную страницу."""
    post_list = get_published_posts()[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def category_posts(request, category_slug):
    """Отображает посты категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = category.posts.select_related(
        'location', 'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now()
    )
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': post_list
    })


def post_detail(request, id):
    """Отображает один пост."""
    post = get_object_or_404(get_published_posts(), pk=id)
    return render(request, 'blog/detail.html', {'post': post})
