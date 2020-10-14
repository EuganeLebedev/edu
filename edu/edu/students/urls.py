from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('register/', views.StudentCreationView.as_view(), name='register_student'),
    path('login/', views.StudentLoginView.as_view(), name='login_student'),
    path('logout/', views.StudentLogoutView.as_view(), name='logout_student')
]
