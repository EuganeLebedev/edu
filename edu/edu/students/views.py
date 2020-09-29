from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView
from .forms import StudentCreationForm, StudentAuthenticationForm
# Create your views here.

class StudentCreationView(CreateView):

    template_name = 'students/students_register.html'
    form_class = StudentCreationForm
    success_url = reverse_lazy('index:index')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(user=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result

class StudentLoginView(FormView):
    template_name = 'students/students_login.html'
    form_class = StudentAuthenticationForm
    success_url = reverse_lazy('index:index')



