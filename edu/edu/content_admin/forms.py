from django import forms
from courses.models import Course, ModuleTest, Answer, Question
from django.forms import inlineformset_factory

class CourseCreateForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['title', 'title_image', 'subject', 'overview']
        labels = {
            'title': 'Заголовок',
            'title_image': 'Изображение',
            'subject': 'Предмет',
            'overview': 'Описание',
        }

class ModuleTestCreateForm(forms.ModelForm):

    class Meta:
        model = ModuleTest
        fields = ['title']
        labels = {
            'title': 'Заголовок',
        }

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ["question"]
        labels = {
            "question": "Вопрос"
        }

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ["answer", "is_correct", ]
        labels = {
            "answer": "Ответ",
            "is_correct": "Правильный?",
        }



AnswerFormset = inlineformset_factory(Question, Answer, form=AnswerForm, extra=1, min_num=3)
