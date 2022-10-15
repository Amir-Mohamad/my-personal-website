from django.contrib import admin
from .models import Article, List
from core.models import Category
from django.contrib.contenttypes.admin import GenericStackedInline

class CategoryStackedInline(GenericStackedInline):
    model = Category
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CategoryStackedInline, ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(List)
