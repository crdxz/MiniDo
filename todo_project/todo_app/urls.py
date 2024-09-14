from django.urls import path 
from . import views 

urlpatterns = [
    path('' , views.TaskList.as_view(), name='task_list'),
    path('task/new/' , views.TaskCreate.as_view() , name='task_new'),
    path('task/<int:pk>/edit/' , views.TaskUpdate.as_view() , name='task_edit'),
    path('task/<int:pk>/delete/' , views.TaskDelete.as_view() , name='task_delete'),

]