from . import views
from django.urls import path


app_name = 'books'
urlpatterns = [
    path('', views.BookList.as_view(), name='list'),
    path('book/<int:id>/<str:slug>', views.BookDetail.as_view(), name='detail'),

    # like
    path('like/<int:book_id>/', views.book_like, name='like'),

]