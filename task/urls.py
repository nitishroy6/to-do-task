from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_controller),
    path('', task_list, name='task_list'),
    path('task-create/', task_create, name='task_create'),
    path('move-to-in-progress/', move_to_in_progress, name='move_to_in_progress'),
    path('move-to-completed/', move_to_completed, name='move_to_in_completed'),
    path('move-to-hold/', move_to_hold, name='move_to_in_hold'),

]
