from blog.validators import validate_cover
from ckeditor.fields import RichTextField
from core.managers import ActiveManager
from core.models import Bookmark, Category
from core.models import Comment
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.db import models
from taggit.managers import TaggableManager


User = get_user_model()

class BooksBaseModel(models.Model):
    updated = models.DateTimeField(auto_now_add=True, verbose_name='کی اپدیت شده ؟')
    created = models.DateTimeField(auto_now=True, verbose_name='کی ساخته شده ؟')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        abstract = True



class Book(BooksBaseModel):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', "منتشر شده"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', verbose_name='کاربر')
    name_en = models.CharField(max_length=300, verbose_name='نام به انگلیسی')
    name_fa = models.CharField(max_length=300, verbose_name='نام به فارسی')
    category = models.ManyToManyField(Category, related_name='categories', verbose_name='دسته بندی')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='شناسه')
    content = RichTextField(verbose_name='توضحیات')
    preview = models.CharField(max_length=500, default='', verbose_name='پیش نمایش')
    cover = models.ImageField(
        upload_to='media/book/', validators=[validate_cover], verbose_name='عکس')
    likes = models.ManyToManyField(
        User, blank=True, related_name='book_like', verbose_name='لایک ها')
    vpn = models.BooleanField(default=False, verbose_name='آیا نیاز به vpn دارد ؟')
    comments = GenericRelation(Comment, content_type_field='parent_content_type', object_id_field='parent_object_id')
    bookmarks = GenericRelation(Bookmark, content_type_field='parent_content_type', object_id_field='parent_object_id')

    objects = models.Manager()
    active = ActiveManager()
    tags = TaggableManager()

    class Meta:
        ordering = ['-id']
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"

    def likes_count(self):
        return self.likes.count()
    
    def __str__(self):
        return self.name_en

