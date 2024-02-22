from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView
from django.views.generic import ListView, UpdateView

from task_manager.apps.users.forms import UserForm, UpdateUserForm
from task_manager.mixins import AuthenticateMixin, PermissionMixin, \
    DeleteProtectionMixin


class UsersView(ListView):
    template_name = 'users/list.html'
    model = get_user_model()
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = _('User has been registered successfully')


# Изменение пользователя
# Изменить
class UserUpdateView(AuthenticateMixin,
                     PermissionMixin,
                     SuccessMessageMixin,
                     UpdateView):
    template_name = 'users/update.html'
    model = get_user_model()
    form_class = UpdateUserForm

    success_url = reverse_lazy('users_list')
    success_message = _('User has been updated successfully')

    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users_list')


class UserDeleteView(AuthenticateMixin,
                     PermissionMixin,
                     DeleteProtectionMixin,
                     SuccessMessageMixin,
                     DeleteView):
    template_name = 'users/delete.html'
    model = get_user_model()

    success_url = reverse_lazy('users_list')
    success_message = _('User has been deleted successfully')

    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users_list')

    rejection_message = _('Unable to delete user because it is in use')
    rejection_url = reverse_lazy('users_list')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
