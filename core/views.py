from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from blog.models import Article
from .models import Comment, Reply, Category


class Home(View):
    template_name = 'core/home.html'

    def get(self, request):
        articles = Article.active.all()

        top_articles = Article.objects.annotate(like_count=Count('likes')).order_by('-like_count')

        return render(request, self.template_name, context={'articles': articles, 'top_articles': top_articles})


@login_required
def comment_create(request):
    if request.method == 'POST':
        parent = get_object_or_404(Article, id=request.POST['id'])
        comment = Comment.objects.create(user=request.user,
            body=request.POST['text'],
            parent=parent
        )
        if request.user.is_authenticated:
            comment.is_active=True
            comment.save()
        # send email and successful response
        return HttpResponse('کامنت شما با موفقیت ثبت شد')
    else:
        return HttpResponse('کرم نریز بجه')
    

@login_required
def reply_create(request):
    if request.method == 'POST':
        comment = Comment.objects.get(id=request.POST['id'])
        reply = Reply.objects.create(user=request.user,
            body=request.POST['text'],
            comment=comment
        )
        if request.user.is_authenticated:
            reply.is_active=True
            reply.save()
        # send email and successful response
        return HttpResponse('کامنت شما با موفقیت ثبت شد')
    else:
        return HttpResponse('کرم نریز بجه')


class CategoryView(View):
    template_name = 'core/category_detail.html'

    def get(self, request, slug):
        category_data = Category.active.get(slug=slug)
        
        print(category_data.articles.all())
        return render(request, self.template_name, context={'category_data': category_data})


class CategoryListView(View):
    template_name = 'core/category_list.html'

    def get(self, request):
        categories = Category.active.all()

        return render(request, self.template_name, context={'categories': categories})


