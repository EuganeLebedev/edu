from django import forms
from courses.models import Course, ModuleTest, Answer, Question
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, Button

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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_tag = True
    #     self.helper.form_class = "form-horizontal"
    #     self.helper.label_class = "col-md-3 create-label"

    class Meta:
        model = Question
        fields = ["question"]

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ["answer", "is_correct", ]


AnswerFormset = inlineformset_factory(Question, Answer, form=AnswerForm, extra=2)
