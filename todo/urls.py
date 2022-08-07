from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('view/<int:id>', views.view, name='view'),
    path('create', views.create, name='create'),
    path('completed/', views.completed, name='completed'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('completed/<int:id>', views.completed_by_id, name='completed')
]
