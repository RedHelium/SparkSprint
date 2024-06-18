from django.urls import path

from apps.tasks.views import add_task, remove_all_tasks, remove_column_tasks, remove_task, update_task

urlpatterns = [
    path("tasks/add", add_task, name="add_task"),
    path("tasks/all/delete", remove_all_tasks, name="remove_all_tasks"),
    path("tasks/column/delete", remove_column_tasks, name="remove_column_tasks"),
    path("tasks/delete", remove_task, name="remove_task"),
    path("tasks/update", update_task, name="update_task"),
]
