from django.views.generic.base import TemplateView

from task_manager.mixins import AuthenticateMixin


class LabelsView(AuthenticateMixin, TemplateView):
    template_name = 'labels/index.html'
