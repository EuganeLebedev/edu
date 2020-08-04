from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.urls import reverse


class NewsModel(models.Model):

    title = models.CharField(max_length=124)
    content = RichTextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')

    class Meta():
        verbose_name = 'news'
        verbose_name_plural = 'news'