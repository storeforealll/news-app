from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('about/', TemplateView.as_view(template_name='news/about.html'), name='about'),
    path('privacy/', TemplateView.as_view(template_name='news/privacy.html'), name='privacy'),
]