from django.views.generic.base import TemplateView

from task_manager.mixins import AuthenticateMixin


class TasksView(AuthenticateMixin, TemplateView):
    template_name = 'tasks/list.html'


class TaskCreateView(AuthenticateMixin, TemplateView):
    template_name = 'tasks/index.html'


class TaskUpdateView(AuthenticateMixin, TemplateView):
    template_name = 'tasks/index.html'


class TaskDeleteView(AuthenticateMixin, TemplateView):
    template_name = 'tasks/index.html'