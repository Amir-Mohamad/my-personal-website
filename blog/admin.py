from django.contrib import admin
from .models import Article, List
from core.models import Category
from django.contrib.contenttypes.admin import GenericStackedInline



# class ArticleAdmin(admin.ModelAdmin):
#     readonly_fields = ['category']
#     fields = ['author','list','title','slug','content','preview','cover','likes','vpn','tags', 'category']
        



admin.site.register(Article)
admin.site.register(List)
