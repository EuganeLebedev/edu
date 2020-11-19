from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView
from .forms import StudentCreationForm, StudentAuthenticationForm
from profiles.models import StudentsGroupModel


# Create your views here.

class StudentCreationView(CreateView):
    template_name = 'students/students_register.html'
    form_class = StudentCreationForm
    success_url = reverse_lazy('students:login_student')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(user=cd['username'], password=cd['password1'])
        if user is not None:
            if user.is_active():
                login(self.request, user)
        return result


class StudentLoginView(LoginView):
    template_name = 'students/students_login.html'
    form_class = StudentAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('index:index')


class StudentLogoutView(LogoutView):
    next_page = 'students:login_student'


class GroupListView(ListView):

    model = StudentsGroupModel
    template_name = 'students/groups/groups_list.html'
