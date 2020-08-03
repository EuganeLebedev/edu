from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.IndexVIew.as_view(), name='index'),
    path('news/', views.NewsListView.as_view(), name='news_list')

]