from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('article/<int:id>/<str:slug>', views.ArticleDetail.as_view(), name='detail'),

    # like
    path('like/<int:article_id>/', views.article_like, name='like'),
]