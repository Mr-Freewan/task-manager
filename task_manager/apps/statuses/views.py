from django.views.generic.base import TemplateView

from task_manager.mixins import AuthenticateMixin


class StatusesView(AuthenticateMixin, TemplateView):
    template_name = 'statuses/index.html'
