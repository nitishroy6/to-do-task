
from .forms import TaskForm
from django.shortcuts import render, redirect,get_object_or_404
from .models import Task
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import ensure_csrf_cookie

class TaskEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Task):
            return {'id': obj.id, 'description': obj.task_description, 'status': obj.task_status}
        return super().default(obj)


#  -- Login Controller --
# @ensure_csrf_cookie
def login_controller(request):
    return render(request,'login.html')
@ensure_csrf_cookie
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return JsonResponse({'success': True, 'task': task}, encoder=TaskEncoder)
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form data'})
    else:
        form = TaskForm()
    return render(request, 'index.html', {'form': form})


@ensure_csrf_cookie
def move_to_in_progress(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids[]')

        try:
            tasks = Task.objects.filter(id__in=task_ids)
            for task in tasks:
                task.task_status = 1
                task.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@ensure_csrf_cookie
def move_to_completed(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids[]')
        try:
            tasks = Task.objects.filter(id__in=task_ids)
            for task in tasks:
                task.task_status = 2
                task.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})
@ensure_csrf_cookie
def move_to_hold(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids[]')
        try:
            tasks = Task.objects.filter(id__in=task_ids)
            for task in tasks:
                task.task_status = 3
                task.save()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})