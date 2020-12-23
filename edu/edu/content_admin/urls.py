from django.urls import path
from . import views

app_name = 'content_admin'

urlpatterns = [
    path('news/create/', views.NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', views.CourseUpdateView.as_view(), name='course_update'),
    path('courses/<int:course_pk>/module/create', views.ModuleCreateView.as_view(), name='module_create'),
    path('courses/<int:course_pk>/module/<int:pk>/update', views.ModuleUpdateView.as_view(), name='module_update'),
    path('courses/<int:course_pk>/module/<int:module_pk>/test_creation', views.ModuleTestCreateView.as_view(),
         name='module_test_create'),
    path('courses/<int:course_pk>/module/<int:module_pk>/test/<int:test_pk>/create',
         views.ModuleTestQuestionCreateView.as_view(),
         name='module_test_question_create'),
    path('test/<int:test_pk>/question_create',
         views.ModuleTestQuestionAnswerCreateView.as_view(), name="answers_create"),
    path('test/<int:test_pk>/question/<int:pk>/question_update', views.ModuleTestQuestionAnswerUpdateView.as_view(), name="answers_update"),

]
