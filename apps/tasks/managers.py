

from django.db.models import Manager

class TaskManager(Manager):
    def add_task(self, header=''):
        task = self.create(name=header)
        
        return task
    