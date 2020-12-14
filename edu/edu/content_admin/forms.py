from django import forms
from courses.models import Course

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


