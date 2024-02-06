from django.views.generic.base import TemplateView


class StatusesView(TemplateView):
    template_name = 'statuses/index.html'