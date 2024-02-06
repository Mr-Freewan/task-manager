from django.views.generic.base import TemplateView


class TasksView(TemplateView):
    template_name = 'tasks/index.html'