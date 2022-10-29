from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from mptt.models import TreeForeignKey, MPTTModel
from .managers import ActiveManager

User = get_user_model()


class CoreBaseModel(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Category(CoreBaseModel, MPTTModel):
    name = models.CharField(max_length=250)
    slug = models.SlugField()

    # object_id = models.IntegerField(default=1)
    # content_type = models.ForeignKey(
    #     ContentType,
    #     on_delete=models.PROTECT,
    # )
    # parent = GenericForeignKey(
    #     'content_type',
    #     'object_id',
    # )
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def is_category_active(self):
        if self.is_active:
            return True
        else:
            return False
    is_category_active.boolean = True

    def __str__(self):
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Comment(CoreBaseModel):
    """
        The main comment model in article and blog pages
    """
    ARTICLE = 'article'
    BOOK = 'book'
    TYPE_CHOICES = (
        (ARTICLE, 'Article'),
        (BOOK, 'Book'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    # article = models.ForeignKey(
    #     Article, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    body = models.CharField(max_length=400, default='')

    parent_object_id = models.IntegerField(default=1)
    parent_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
    )
    parent = GenericForeignKey(
        'parent_content_type',
        'parent_object_id',
    )

    objects = models.Manager()
    active = ActiveManager()

    def is_comment_active(self):
        if self.is_active:
            return True
        else:
            return False
    is_comment_active.boolean = True

    def __str__(self):
        return self.body[:20]


class Reply(CoreBaseModel):
    """
        Used for making replies on comments in articles and blogs
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="replies")
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="replies")
    body = models.TextField(max_length=400)

    def __str__(self):
        return self.body


class Bookmark(CoreBaseModel):
    ARTICLE = 'article'
    BOOK = 'book'
    TYPE_CHOICES = (
        (ARTICLE, 'Article'),
        (BOOK, 'Book'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_object_id = models.IntegerField(default=1)
    parent_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.PROTECT,
    )
    parent = GenericForeignKey(
        'parent_content_type',
        'parent_object_id',
    )

    objects = models.Manager()
    active = ActiveManager()

    def __str__(self):
        return f'{self.user} -> {self.parent}'