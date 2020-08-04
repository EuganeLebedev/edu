from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from index.models import NewsModel


class NewsCreateView(CreateView):
    model = NewsModel
    fields = ['title', 'content']
    template_name = 'content_admin/news_create.html'
