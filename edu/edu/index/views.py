from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from . import models


class IndexVIew(TemplateView):
    template_name = 'index/index.html'


class NewsListView(ListView):
    template_name = 'index/news_list.html'
    model = models.NewsModel
    context_object_name = 'news'