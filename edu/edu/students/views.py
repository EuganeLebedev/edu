from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView
from .forms import StudentCreationForm, StudentAuthenticationForm, StudentsGroupCreateForm
from profiles.models import StudentsGroupModel, UserModel
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


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

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            username = request.GET.get('username', None)
            responce = {"is_taken": UserModel.objects.filter(username__iexact=username).exists()}
            return JsonResponse(responce)

        return super(StudentCreationView, self).get(request, *args, **kwargs)


class StudentLoginView(LoginView):
    template_name = 'students/students_login.html'
    form_class = StudentAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('index:index')


class StudentLogoutView(LogoutView):
    next_page = 'students:login_student'


class GroupListView(PermissionRequiredMixin, ListView):

    model = StudentsGroupModel
    template_name = 'students/groups/groups_list.html'
    paginate_by = 10

    permission_required = 'is_staff'

    def get_queryset(self, **kwargs):
        qs = super(GroupListView, self).get_queryset(**kwargs)
        qs = qs.prefetch_related("usermodel_set").select_related('course')
        return qs



class GroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    model = StudentsGroupModel
    template_name = 'students/groups/group_create.html'
    permission_required = 'is_staff'
    form_class = StudentsGroupCreateForm

class GroupUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    model = StudentsGroupModel
    template_name = 'students/groups/group_update.html'
    permission_required = 'is_staff'
    form_class = StudentsGroupCreateForm

    def get_queryset(self, **kwargs):
        qs = super(GroupUpdateView, self).get_queryset(**kwargs)
        qs =qs.prefetch_related("usermodel_set").select_related('course')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        group_users = context.get('object').usermodel_set.all().order_by('id')
        context["group_users"] = group_users

        context["all_users"] = UserModel.objects.exclude(id__in=group_users).order_by('id')

        return context

