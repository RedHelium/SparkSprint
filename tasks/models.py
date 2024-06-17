from django.db import models

from tasks.managers import TaskManager

# Create your models here.


class TaskColumn(models.Model):

    name = models.CharField(verbose_name='Заголовок', max_length = 32)
    max_task = models.IntegerField(verbose_name='Макс. кол-во задач', null=True, blank=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Столбец задач'
        verbose_name_plural = 'Столбцы задач'
        
        
class Task(models.Model):
    
    name = models.CharField(verbose_name='Заголовок', max_length = 150)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    column = models.ForeignKey(TaskColumn, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    
    objects = TaskManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ["-created"]