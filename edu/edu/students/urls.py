from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('register/', views.StudentCreationView.as_view(), name='register_student'),
    path('login/', views.StudentLoginView.as_view(), name='login_student'),
    path('logout/', views.StudentLogoutView.as_view(), name='logout_student'),
    path('groups/', views.GroupListView.as_view(), name='student_groups'),
    path('group/create', views.GroupCreateView.as_view(), name='group_create'),
    path('group/<int:pk>/update', views.GroupUpdateView.as_view(), name='group_update'),
    path('group/<int:pk>', views.GroupDetailView.as_view(), name='group_detail'),
    path('groupstatus/<int:pk>/change', views.ChangeGroupStatus.as_view(), name='group_status_change'),
]
