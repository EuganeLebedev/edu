from django.shortcuts import render
from .forms import CourseCreateForm

# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
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

class CourseCreateView(CreateView):

    template_name = 'content_admin/course_detail.html'
    form_class = CourseCreateForm

    def form_valid(self, form):

        course = form.save(commit=False)
        course.owner = self.request.user
        course.save()
        return super().form_valid(form)

class CourseUpdateView(UpdateView):

    template_name = 'content_admin/course_detail.html'
    form_class = CourseCreateForm