from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from profiles.models import UserModel

class StudentCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2', 'phone_number']

class StudentAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):




    class Meta:
        model = UserModel
        fields = ['username', 'password1']