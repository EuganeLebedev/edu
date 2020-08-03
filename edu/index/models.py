from django.db import models

# Create your models here.

class NewsModel(models.Model):

    title = models.CharField(max_length=124)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'news'
        verbose_name_plural = 'news'