from django.contrib import admin

from task_manager.apps.statuses.models import Status

admin.site.register(Status)
