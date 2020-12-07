from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from profiles.models import UserModel

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

