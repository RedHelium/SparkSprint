from django import template
from tasks.models import Task


register = template.Library()

@register.inclusion_tag('accounts/includes/tasks.html')
def get_tasks_by_column(column):

    tasks = Task.objects.filter(column=column)
    
    return {'tasks': tasks, 'column': column}