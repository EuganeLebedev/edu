from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView
from index.models import NewsModel


class NewsCreateView(CreateView):
    model = NewsModel
    fields = ['title', 'title_image', 'content']
    template_name = 'content_admin/news_create.html'

class NewsUpdateView(UpdateView):
    model = NewsModel
    fields = ['title', 'title_image', 'content']
    template_name = 'content_admin/news_create.html'

class NewsDeleteView(DeleteView):
    model = NewsModel
    template_name = 'content_admin/news_delete.html'

