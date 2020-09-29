from django import forms
from .models import NewsModel

class NewsDetailForm(forms.ModelForm):

    class Meta:
        model = NewsModel
        fields = ['title', 'title_image', 'content', 'create_date', 'update_date']


