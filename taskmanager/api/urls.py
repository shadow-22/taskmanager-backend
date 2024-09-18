from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('tasks/', views.task_list_create, name='task_list_create'),  # Single view for both GET and POST
    path('tasks/<int:task_id>/', views.update_or_delete_task, name='task_update_or_delete'),
]