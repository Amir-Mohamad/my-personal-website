from django.db import models
from blog.models.base import BlogBaseModel


class List(BlogBaseModel):
    name = models.CharField(max_length=250, verbose_name='نام')
    description = models.TextField(verbose_name='توضیحات')

    class Meta:
        verbose_name = 'لیست'
        verbose_name = 'لیست ها'

    def __str__(self):
        return self.name
