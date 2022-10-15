from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.shortcuts import get_object_or_404, HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required

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


@login_required
def article_like(request, article_id):
    """
    
    NOTE:
        Why we cant use ploymorphism in this function ?
         - in this case we should return a response that uses the article/parent data
         - and if we use ploymorphism we cant access to the detailed data in each instance
         - (becuase of differnt names in each response: article/book/parent).
    """
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)

        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)

        data = article.likes.count()
        return render(request, 'blog/partials/like.html', context={'article': article})
    else:
        return HttpResponse('به ارور برخوردیم. بعدا تلاش کن')