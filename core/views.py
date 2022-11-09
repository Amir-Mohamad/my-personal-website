from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count
from django.shortcuts import HttpResponse, get_object_or_404
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic import View
from .models import Bookmark, Comment, Reply, Category
from blog.models import Article


class Home(View):
    template_name = 'core/home.html'

    def get(self, request):
        articles = Article.active.all()

        top_articles = Article.objects.annotate(like_count=Count('likes')).order_by('-like_count')

        return render(request, self.template_name, context={'articles': articles, 'top_articles': top_articles})


@login_required
@require_POST
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
@require_POST
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

@login_required
@require_POST
def bookmark_create(request, article_id):
    if request.method == 'POST':
    
        parent = get_object_or_404(Article, id=article_id)

        parent_content_type=ContentType.objects.get_for_model(parent)

        if type == 'article':
            parent = get_object_or_404(Article, id=article_id)
        else:
            pass
        bookmark = Bookmark.objects.filter(user=request.user, parent_object_id=parent.id, parent_content_type=parent_content_type) 
        if bookmark.exists():
            bookmark.delete()
            print('deleted')
        else:
            Bookmark.objects.create(user=request.user, parent_object_id=parent.id, parent_content_type=parent_content_type)
            print('created')

        return HttpResponse('بنازم. نشان گذاری شد.')
    else:
        return HttpResponse('به ارور برخوردیم')