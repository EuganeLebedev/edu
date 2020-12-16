from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .forms import CourseCreateForm, ModuleTestCreateForm, AnswerFormset

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
        module = get_object_or_404(Module, pk = self.kwargs.get("module_pk"))
        form.instance.module = module
        return super(ModuleTestCreateView, self).form_valid(form)

class ModuleTestQuestionCreateView(CreateView):
    model = Question
    fields = ["question",]
    template_name = "content_admin/module_test_question_create.html"
    #TODO
    #Перенаправить на окно создания ответов к этому вопросу
    success_url = reverse_lazy("index:index")
    
    def form_valid(self, form):
        module_test = get_object_or_404(ModuleTest, pk=self.kwargs.get("test_pk"))
        form.instance.module_test = module_test
        return super(ModuleTestQuestioncreateView, self).form_valid(form)


class ModuleTestQuestionAnswerCreateView(CreateView):
    model = Question
    fields = ['question',]
    success_url = reverse_lazy('index')
    template_name = "content_admin/answers_create.html"

    def get_context_data(self, **kwargs):
        data = super(ModuleTestQuestionAnswerCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            print("POST")
            data['answers'] = AnswerFormset(self.request.POST)
        else:
            data['answers'] = AnswerFormset()
        return data


    def form_valid(self, form):
        print("VAliD")
        context = self.get_context_data()
        answers = context['answers']
        with transaction.atomic():
            self.object = form.save()

            if answers.is_valid():
                answers.instance = self.object
                answers.save()
        return super(ModuleTestQuestionAnswerCreateView, self).form_valid(form)