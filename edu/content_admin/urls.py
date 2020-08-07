from django.urls import path
from . import views

app_name = 'content_admin'

urlpatterns = [
    path('news/create/', views.NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name = 'mews_delete'),

]