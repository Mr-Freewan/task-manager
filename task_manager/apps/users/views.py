from django.views.generic.base import TemplateView


class UsersView(TemplateView):
    template_name = 'users/index.html'
