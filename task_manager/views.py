from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('start_page')
    success_message = gettext_lazy('You are logged in')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('start_page')
    success_message = gettext_lazy('You are logged out')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, gettext_lazy('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
