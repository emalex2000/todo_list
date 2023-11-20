from django.urls import path 
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('todo_list', views.TodoPage.as_view(), name='todolist'),
    path('create-tasks', views.TodoCreate.as_view(), name='create-tasks'),
    path('item/<int:pk>/', views.TodoDetail.as_view(), name='item'),
    path('edit/<int:pk>/view', views.TodoUpdate.as_view(), name='edit'),
]