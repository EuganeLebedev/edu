from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from profiles.models import UserModel, StudentsGroupModel
from courses.models import Course
from django.contrib.admin.widgets import FilteredSelectMultiple

class StudentCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Пользователь'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя'})
        self.fields['first_name'].required = True
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Фамилия'})
        self.fields['last_name'].required = True
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Номер телефона'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control',  'placeholder': 'Пароль повторно'})


    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name','password1', 'password2', 'phone_number']
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
            'phone_number': 'Номер телефона'

        }
        #hepl_texts = {}


class StudentAuthenticationForm(AuthenticationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Пользователь'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль'})

    class Meta:
        model = UserModel
        fields = ['username', 'password1']
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',

        }


class StudentsGroupCreateForm(forms.ModelForm):
    usermodel_set = forms.ModelMultipleChoiceField(queryset=UserModel.objects.filter(is_active=True), required=False,
                                           widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = StudentsGroupModel
        fields = ['group_code', 'start_date', 'course', 'usermodel_set']

        widgets = {
            'start_date' : forms.DateInput(format=('%m/%d/%Y'), attrs={
                'class': 'form-control', 'placeholder': 'Выберите дату начала', 'type': 'date'
            }),
            'group_code': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Код группы'
        }),
            'course': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        for usermodel in self.cleaned_data.get("usermodel_set"):
            usermodel.group_code.add(self.instance)
        return self.instance

