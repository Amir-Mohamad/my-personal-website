from ckeditor.fields import RichTextField
from core.managers import ActiveManager
from django.contrib.auth import get_user_model
from django.db import models
from taggit.managers import TaggableManager
from blog.validators import validate_cover
from blog.models.base import BlogBaseModel
from blog.models.list import List
from core.models import Category
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey

from core.models import Comment

User = get_user_model()


class Article(BlogBaseModel):
    """
        NOTE: 
            - The author field must be null because of on_delete
    """
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', "منتشر شده"),
    )
    author = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='نویسنده')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی')
    list = models.ForeignKey(
        List, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='لیست')
    title = models.CharField(max_length=250, verbose_name='عنوان')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='شناسه')
    content = RichTextField(verbose_name='توضحیات')
    preview = models.CharField(max_length=500, default='', verbose_name='پیش نمایش')
    cover = models.ImageField(
        upload_to='media/article/', validators=[validate_cover], verbose_name='عکس')
    likes = models.ManyToManyField(
        User, blank=True, related_name='article_like', verbose_name='لایک ها')
    vpn = models.BooleanField(default=False, verbose_name='آیا نیاز به vpn دارد ؟')
    comments = GenericRelation(Comment, content_type_field='parent_content_type', object_id_field='parent_object_id')
    objects = models.Manager()
    active = ActiveManager()
    tags = TaggableManager()

    class Meta:
        ordering = ['-id']
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def likes_count(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title
