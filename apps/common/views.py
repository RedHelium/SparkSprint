from django.shortcuts import render

from apps.tasks.models import TaskColumn

# Create your views here.

def home(request):
    
    columns = TaskColumn.objects.all()
    
    
    return render(request, 'accounts/home.html', {'columns': columns})