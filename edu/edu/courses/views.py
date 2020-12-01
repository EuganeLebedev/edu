from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
import json

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


    def get_context_data(self, *args, **kwargs):
        context = super(ModuleTestDetailView, self).get_context_data(*args, **kwargs)
        question_set = context[self.context_object_name].question_set.all()
        answer_count = models.StudentAnswer.objects.filter(user=self.request.user, question__in=question_set).count()
        context["answers_count"] = answer_count
        context["questions_count"] = question_set.count()
        context["progress"] = int((answer_count/question_set.count())*100)
        return context

    def get(self, request, *args, **kwargs):
        #TODO
        # 1. Работа с несколькими правильными ответами

        if request.is_ajax():
            print(request.GET.get('my_answer'))
            answer_list_deserialized = request.GET.get('my_answer')
            return_answers = {}
            if answer_list_deserialized:
                answer = json.loads(answer_list_deserialized)
                print(f'{answer=}', type(answer))
                answer_model = models.Answer.objects.get(id=answer.get('answer_id'))
                question_model = models.Question.objects.get(id=answer.get('question_id'))

                print(f'{answer_model.is_correct=}')
                return_answers.update({'answer_id': answer_model.id, 'is_correct': answer_model.is_correct})
                if request.user.is_authenticated:

                    try:
                        obj = models.StudentAnswer.objects.get(user=request.user, question=question_model)
                        print('EXIST')
                        obj.answer=answer_model
                        obj.save()
                    except models.StudentAnswer.DoesNotExist:
                        student_answer = models.StudentAnswer.objects.create(user=request.user,
                                                                                   question=question_model,
                                                                                   answer=answer_model)

            else:
                print('wrong answer_list variable')
            return JsonResponse({'seconds': 1, 'checked_answer': return_answers}, status=200)

        return super().get(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        print(dict(self.request.POST))
        print(f'args {args}')
        return HttpResponse(f"<h1>OK</h1>"
                            f"kwargs: {kwargs}"
                            f"<hr>request data: {dict(self.request.POST) }")

