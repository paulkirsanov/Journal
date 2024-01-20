from django.db import models
from django.urls import reverse


class BlogForm(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', null=True)

    class Meta:
        verbose_name = 'Мой блог'
        verbose_name_plural = 'Мой блог'
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
