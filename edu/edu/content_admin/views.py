from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse

from .forms import CourseCreateForm, ModuleTestCreateForm, AnswerFormset, QuestionForm

# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from index.models import NewsModel
from courses.models import Course, Module, Question, ModuleTest, Answer


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
    model = Course
    template_name = 'content_admin/course_detail.html'
    form_class = CourseCreateForm


class ModuleCreateView(CreateView):
    model = Module
    fields = ["title", "content", "description"]
    template_name = "content_admin/module_create.html"

    def form_valid(self, form):
        course = get_object_or_404(Course, pk=self.kwargs.get("course_pk"))
        form.instance.owner = self.request.user
        form.instance.course = course
        return super(ModuleCreateView, self).form_valid(form)


class ModuleUpdateView(UpdateView):
    model = Module
    fields = ["title", "content", "description"]
    template_name = "content_admin/module_create.html"


class ModuleTestCreateView(CreateView):
    form_class = ModuleTestCreateForm
    template_name = "content_admin/module_test_create.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        module = get_object_or_404(Module, pk=self.kwargs.get("module_pk"))
        form.instance.module = module
        return super(ModuleTestCreateView, self).form_valid(form)




class ModuleTestQuestionAnswerCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    success_url = None
    template_name = "content_admin/answers_create.html"

    def get_success_url(self):
        success_url = reverse("courses:module_test", kwargs={"pk": self.object.module_test.id})
        return success_url

    def get_context_data(self, **kwargs):
        data = super(ModuleTestQuestionAnswerCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['answers'] = AnswerFormset(self.request.POST)
        else:
            data['answers'] = AnswerFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        module_test = get_object_or_404(ModuleTest, pk=self.kwargs.get("test_pk"))
        form.instance.module_test = module_test
        answers = context['answers']
        with transaction.atomic():
            self.object = form.save()

            if answers.is_valid():
                answers.instance = self.object
                answers.save()
        return super(ModuleTestQuestionAnswerCreateView, self).form_valid(form)

class ModuleTestQuestionAnswerUpdateView(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = "content_admin/answers_create.html"
    success_url = None

    def get_success_url(self):
        success_url = reverse("courses:module_test", kwargs={"pk": self.object.module_test.id})
        return success_url

    def get_context_data(self, **kwargs):
        data = super(ModuleTestQuestionAnswerUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['answers'] = AnswerFormset(self.request.POST, instance=self.object)
        else:
            data['answers'] = AnswerFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        module_test = get_object_or_404(ModuleTest, pk=self.kwargs.get("test_pk"))
        form.instance.module_test = module_test
        answers = context['answers']
        with transaction.atomic():
            self.object = form.save()

            if answers.is_valid():
                answers.instance = self.object
                answers.save()
        return super(ModuleTestQuestionAnswerUpdateView, self).form_valid(form)

