from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from profiles.models import StudentsGroupModel
from courses.models import StudentAnswer, Question, ModuleTest, Module
import json

from . import models


# Create your views here.

class CourseDetailView(DetailView):
    model = models.Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'


class CoursesListView(ListView):
    model = models.Course
    # context_object_name = 'courses'
    template_name = 'courses/courses_list.html'


class ModuleDetailView(LoginRequiredMixin, DetailView):
    model = models.Module
    context_object_name = 'module'
    template_name = 'courses/module/module_detail.html'


class ModuleTestDetailView(LoginRequiredMixin, DetailView):
    model = models.ModuleTest
    template_name = 'courses/module/module_test_detail.html'
    context_object_name = 'test'

    def get_queryset(self):
        qs = super(ModuleTestDetailView, self).get_queryset()
        qs = qs.select_related()
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(ModuleTestDetailView, self).get_context_data(*args, **kwargs)
        question_set = context[self.context_object_name].question_set.all().select_related()
        answer_count = models.StudentAnswer.objects.filter(user=self.request.user,
                                                           question__in=question_set).count()
        context["answers_count"] = answer_count
        questions_count = question_set.count()
        context["questions_count"] = questions_count
        context["progress"] = int((answer_count / questions_count) * 100) if questions_count > 0 else 0

        try:
            module_status = models.StudentModuleTestStatus.objects.get(user=self.request.user,
                                                                       module_test=self.get_object())
        except models.StudentModuleTestStatus.DoesNotExist:
            module_status = models.StudentModuleTestStatus.objects.create(user=self.request.user,
                                                                          module_test=self.get_object())
        context["module_test_status"] = module_status
        return context

    def get(self, request, *args, **kwargs):
        # TODO
        # 1. Работа с несколькими правильными ответами

        if request.is_ajax():
            answer_list_deserialized = request.GET.get('my_answer')
            return_answers = {}
            if answer_list_deserialized:
                answer = json.loads(answer_list_deserialized)
                answer_model = models.Answer.objects.get(id=answer.get('answer_id'))
                question_model = models.Question.objects.get(id=answer.get('question_id'))
                return_answers.update({'answer_id': answer_model.id, 'is_correct': answer_model.is_correct})
                if request.user.is_authenticated:

                    try:
                        obj = models.StudentAnswer.objects.get(user=request.user, question=question_model)
                        obj.answer = answer_model
                        obj.save()
                    except models.StudentAnswer.DoesNotExist:
                        student_answer = models.StudentAnswer.objects.create(user=request.user,
                                                                             question=question_model,
                                                                             answer=answer_model)
                    questions_set = question_model.module_test.question_set
                    questions_set_count = questions_set.count()

                    answer_count = models.StudentAnswer.objects.filter(user=self.request.user,
                                                                       question__in=questions_set.all()).count()

                    progress = int(int(answer_count) / int(questions_set_count) * 100)
                    module_status = models.StudentModuleTestStatus.objects.get(user=self.request.user,
                                                                               module_test=question_model.module_test)
                    if answer_count == questions_set_count:
                        module_status.passed = True
                        module_status.save()


            else:
                # TODO
                # return message
                print('wrong answer_list variable')
            # context = self.get_context_data(*args, **kwargs)
            # print(f'COUNTS {context.get("questions_count")} {context.get("answers_count")}')
            return JsonResponse(
                {'seconds': 1, 'checked_answer': return_answers, 'progress': progress, 'answer_count': answer_count},
                status=200)

        return super().get(request, *args, **kwargs)


class StudentProgress(TemplateView):
    template_name = 'courses/student_progress.html'

    def get_context_data(self, group_code=None, **kwargs):
        context = super(StudentProgress, self).get_context_data(**kwargs)
        print(kwargs, group_code)
        course = get_object_or_404(StudentsGroupModel, group_code=group_code).course
        module_set = Module.objects.filter(course=course)
        module_test_set = ModuleTest.objects.filter(module__in=module_set)
        question_set = Question.objects.filter(module_test__in=module_test_set)
        answer_set = StudentAnswer.objects.select_related('answer__question', 'user').filter(Q(user=self.request.user), Q(question__in=question_set))
        #queryset = models.StudentModuleTestStatus.objects.select_related('module_test__module__course').filter(user=self.request.user,
        #                                                                                       module_test__module__course=course,
        #                                                                                        module_test__question__studentanswer__user=self.request.user)
        #context['test'] = queryset
        context['answer_set'] = answer_set

        return context
