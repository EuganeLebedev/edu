from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from profiles.models import UserModel

class StudentCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control is-valid'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2', 'phone_number']
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
            'phone_number': 'Номер телефона'

        }
        #hepl_texts = {}


class StudentAuthenticationForm(AuthenticationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control is-valid'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = UserModel
        fields = ['username', 'password1']
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',

        }

