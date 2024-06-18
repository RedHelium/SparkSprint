import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from apps.common.views import home
from apps.tasks.models import Task, TaskColumn

# Create your views here.

def add_task(request):
    
    column = request.POST.get('column')
    
    col = TaskColumn.objects.get(id=column)
    max_tasks = col.max_task
    current_tasks = Task.objects.filter(column=column).count()
    
    if current_tasks < max_tasks:
        Task.objects.create(name='New task', column=col)
    else:
        print('Max limit!') #TODO replace on message
    
    return redirect(home)

def update_task(request):
    
    task = request.POST.get('task')

    name = request.POST.get('name')
    description = request.POST.get('description')
    column = request.POST.get('column')
    
    taskObj = Task.objects.get(id=task)
    col = TaskColumn.objects.get(id=column)
    
    if taskObj.column != col:
        max_tasks = col.max_task
        current_tasks = Task.objects.filter(column=column).count()
        
        if current_tasks < max_tasks:
            taskObj.column = col
        else:
            print("Max limit!") #TODO replace on message
        
    
    taskObj.name = name
    taskObj.description = description
    
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