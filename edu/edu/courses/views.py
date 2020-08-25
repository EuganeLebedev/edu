from django.shortcuts import render
from django.views.generic import DetailView, ListView

from . import models

# Create your views here.

class CourseDetailView(DetailView):
    model = models.Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

class CoursesListView(ListView):
    model = models.Course
    #context_object_name = 'courses'
    template_name = 'courses/courses_list.html'


class ModuleDetailView(DetailView):
    model = models.Module
    context_object_name = 'module'
    template_name = 'courses/module/module_detail.html'


class ModuleTestDetailView(DetailView):
    model = models.ModuleTest
    template_name = 'courses/module/module_test_detail.html'
    context_object_name = 'test'

