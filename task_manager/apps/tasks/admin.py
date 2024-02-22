from django.contrib import admin

from task_manager.apps.tasks.models import Task

# Register your models here.
admin.site.register(Task)
