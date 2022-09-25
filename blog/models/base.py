from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BlogBaseModel(models.Model):
    """
        Some usefull fieds that we use alot in models
    """
    updated = models.DateTimeField(auto_now_add=True, verbose_name='کی اپدیت شده ؟')
    created = models.DateTimeField(auto_now=True, verbose_name='کی ساخته شده ؟')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    class Meta:
        abstract = True
