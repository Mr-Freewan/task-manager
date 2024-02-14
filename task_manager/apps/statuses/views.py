from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from task_manager.apps.statuses.forms import StatusForm
from task_manager.mixins import AuthenticateMixin, DeleteProtectionMixin
from task_manager.apps.statuses.models import Status


class StatusesView(AuthenticateMixin, ListView):
    template_name = 'statuses/list.html'
    model = Status
    context_object_name = 'statuses'


class StatusCreateView(AuthenticateMixin, SuccessMessageMixin, CreateView):
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status created successfully')


class StatusUpdateView(AuthenticateMixin, SuccessMessageMixin, UpdateView):
    template_name = 'statuses/update.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status updated successfully')


class StatusDeleteView(AuthenticateMixin, DeleteProtectionMixin,
                       SuccessMessageMixin, DeleteView):
    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses_list')
    success_message = _('Status deleted successfully')
    rejection_message = _('Unable to delete status because it is in use')
    rejection_url = reverse_lazy('statuses_list')