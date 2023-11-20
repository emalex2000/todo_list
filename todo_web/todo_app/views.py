from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import TodoList
from .forms import TodoForm



class TodoCreate(CreateView):
    model = TodoList
    form_class = TodoForm
    template_name = 'todo_app/todo-create.html'
    success_url = 'todo_list'

class TodoPage(ListView):
    model = TodoList
    template_name = 'todo_app/todolist_list.html'
    context_object_name = 'tasks'

class TodoDetail(DetailView):
    model = TodoList
    template_name = 'todo_app/todo-detail.html'
    context_object_name = 'tasks'


class TodoUpdate(UpdateView):
    model = TodoList
    context_object_name = 'tasks' 
    template_name = 'todo_app/todo-update.html'
    form_class = TodoForm
    success_url = reverse_lazy('todo_list')
