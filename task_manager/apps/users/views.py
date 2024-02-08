from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from task_manager.apps.users.forms import UserForm


class UsersView(TemplateView):
    template_name = 'users/index.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = 'User has been successfully registered'
