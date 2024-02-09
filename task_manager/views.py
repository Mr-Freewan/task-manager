from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    # Used basic AuthenticationForm
    template_name = 'login.html'
    next_page = reverse_lazy('start_page')
    success_message = _('You are logged in')


class UserLogoutView(LogoutView):
    template_name = None
    next_page = reverse_lazy('start_page')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
