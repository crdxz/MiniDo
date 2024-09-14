from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task 
    context_object_name = 'tasks'

class TaskCreate(CreateView): 
    model = Task 
    fields = ['title' , 'description']
    success_url = reverse_lazy('task_list')

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title' , 'description' , 'completed']
    success_url = reverse_lazy('task_list')

class TaskDelete(DeleteView):
    model = Task 
    success_url = reverse_lazy('task_list')

    