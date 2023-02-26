from django.contrib import admin
from .models import Article, List
from core.models import Category
from django.contrib.contenttypes.admin import GenericStackedInline



admin.site.register(Article)
admin.site.register(List)
