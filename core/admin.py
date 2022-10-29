from django.contrib import admin
from .models import Comment, Reply, Category, Bookmark



admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Bookmark)