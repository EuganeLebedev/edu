from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
    path('', views.CoursesListView.as_view(), name='courses_list'),
    path('module/<int:pk>', views.ModuleDetailView.as_view(), name='module_detail'),
    path('test/<int:pk>', views.ModuleTestDetailView.as_view(), name='module_test')
]