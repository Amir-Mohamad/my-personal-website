from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import HttpResponse, get_object_or_404
from blog.models import Article
from django.contrib.auth.decorators import login_required
from .models import Comment


class Home(View):
    template_name = 'core/home.html'

    def get(self, request):
        articles = Article.active.all()

        return render(request, self.template_name, context={'articles': articles})


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
        # send email and successfull response
        return HttpResponse('کامنت شما با موفقیت ثبت شد')
    else:
        return HttpResponse('کرم نریز بجه')