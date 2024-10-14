from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    content = models.TextField(verbose_name='متن')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', verbose_name='نویسنده')

    def __str__(self):
        return self.title
