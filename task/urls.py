from django.urls import path
from .views import task_list, task_create, move_to_in_progress, move_to_completed

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task-create/', task_create, name='task_create'),
    path('move-to-in-progress/', move_to_in_progress, name='move_to_in_progress'),
    path('move-to-completed/', move_to_completed, name='move_to_in_progress'),

]
