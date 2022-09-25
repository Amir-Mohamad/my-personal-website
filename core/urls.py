from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),

    # comment
    path('comment-create/', views.comment_create, name='comment-create'),
]