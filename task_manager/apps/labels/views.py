from django.views.generic.base import TemplateView


class LabelsView(TemplateView):
    template_name = 'labels/index.html'
