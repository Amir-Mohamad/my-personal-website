from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from core.models import Comment
from .models import Article


class ArticleList(View):
    """
        Shows all blog posts by their is_active field
    """
    template_name = 'blog/articles.html'

    def get(self, request):

        articles = Article.active.all()

        return render(request, self.template_name, context={'articles': articles})


class ArticleDetail(View):
    """
        Single blog post
        NOTE:
            - filter by is_active
    """
    template_name = 'blog/article_detail.html'

    def get(self, request, id, slug):
        article = get_object_or_404(Article, slug=slug, pk=id)
        # parent_content_type=ContentType.objects.get_for_model(article)

        # comments = Comment.active.filter(parent=article)

        return render(request, self.template_name, context={'article': article})