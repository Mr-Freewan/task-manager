from django.views.generic.base import TemplateView

from task_manager.mixins import AuthenticateMixin


class TasksView(AuthenticateMixin, TemplateView):
    template_name = 'tasks/index.html'
