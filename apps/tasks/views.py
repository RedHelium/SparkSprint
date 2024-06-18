import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from apps.common.views import home
from apps.tasks.models import Task, TaskColumn

# Create your views here.

def add_task(request):
    
    column = request.POST.get('column')
    
    Task.objects.create(name='New task', column=TaskColumn.objects.get(id=column))
    
    return redirect(home)

def update_task(request):
    
    task = request.POST.get('task')

    name = request.POST.get('name')
    description = request.POST.get('description')
    column = request.POST.get('column')
    
    taskObj = Task.objects.get(id=task)
    
    taskObj.name = name
    taskObj.description = description
    taskObj.column = TaskColumn.objects.get(id=column)
    
    taskObj.save()
    
    return redirect(home)
    

def remove_task(request):
    
    task = request.POST.get('task')
    
    Task.objects.get(id=task).delete()
    
    return redirect(home)


def remove_column_tasks(request):
    
    column = request.POST.get('column')
    
    Task.objects.filter(column=column).delete()
    
    return redirect(home)


def remove_all_tasks(request):
    
    Task.objects.all().delete()
    
    return redirect(home)