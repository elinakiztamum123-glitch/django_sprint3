"""Настройки админ-панели для приложения blog."""
from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс настройки админки для категорий."""

    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Класс настройки админки для местоположений."""

    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Класс настройки админки для публикаций."""

    pass
