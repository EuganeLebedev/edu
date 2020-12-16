from django import forms
from courses.models import Course, ModuleTest

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

