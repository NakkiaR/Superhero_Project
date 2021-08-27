from django.urls import path
from django.contrib import admin

from .import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('edit/', views.edit, name='edit')
]
