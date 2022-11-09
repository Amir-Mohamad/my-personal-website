from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic import View
from core.models import Category
from .models import Article



class ArticleList(View):
    """
        Shows all blog posts by is_active field
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
@require_POST
def article_like(request, article_id):
    """
    
    NOTE:
        Why we cant use polymorphism in this function ?
         - in this case we should return a response that uses the article/parent data
         - and if we use polymorphism we cant access to the detailed data in each instance
         - (because of different names in each response: article/book/parent).
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

