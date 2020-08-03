from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_date', 'update_date')
    #pass