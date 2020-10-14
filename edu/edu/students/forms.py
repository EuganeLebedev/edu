from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from profiles.models import UserModel

class StudentCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control is-valid'})


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

    class Meta:
        model = UserModel
        fields = ['username', 'password1']
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',

        }

