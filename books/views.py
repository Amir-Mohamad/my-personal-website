from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_POST
from .models import Book


# Create your views here.
class BookList(View):
    template_name = 'books/books.html'

    def get(self, request):
        books = Book.active.all()
        return render(request, self.template_name, context={'books': books})
    

class BookDetail(View):
    """
        Single book post
        NOTE:
            - filter by is_active
    """
    template_name = 'books/book_detail.html'

    def get(self, request, id, slug):
        book = get_object_or_404(Book, slug=slug, pk=id)

        return render(request, self.template_name, context={'book': book})


@login_required
@require_POST
def book_like(request, book_id):
    """
    
    NOTE:
        Why we cant use polymorphism in this function ?
         - in this case we should return a response that uses the book/parent data
         - and if we use polymorphism we cant access to the detailed data in each instance
         - (because of different names in each response: book/book/parent).
    """
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)

        if book.likes.filter(id=request.user.id).exists():
            book.likes.remove(request.user)
        else:
            book.likes.add(request.user)

        data = book.likes.count()
        return render(request, 'books/partials/like.html', context={'book': book})
    else:
        return HttpResponse('به ارور برخوردیم. بعدا تلاش کن')

