
from .forms import TaskForm
from django.shortcuts import render, redirect,get_object_or_404
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return render(request, 'task_form.html', {'form': form})
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})



def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'PUT':
        form = TaskForm(request.PUT, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            status = request.PUT.get('task_status')
            task.task_status = status
            task.save()
            return redirect('task_list')

    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})