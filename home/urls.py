from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    #path('admin/',views.admin, name='admin'),
    path('', views.home, name='home'),
    path('tasks', views.task, name='tasks')
]
