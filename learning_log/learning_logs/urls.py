"""Defines URL patterns for learning_logs."""
from django.urls import path
# from django.conf.urls import url
from . import views

app_name = 'main_app'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    # url(r'^$',views.index, name='index'),
]