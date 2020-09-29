from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.StudentCreationView.as_view(), name='register_student'),
    path('login/', views.StudentLoginView.as_view(), name='login_student')
]
