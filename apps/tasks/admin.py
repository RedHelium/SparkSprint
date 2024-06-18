from django.contrib import admin

from apps.tasks.models import Task, TaskColumn

# Register your models here.

@admin.register(TaskColumn)
class TaskColumnAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name',)
