from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from task_manager.apps.labels.forms import LabelForm
from task_manager.apps.labels.models import Label
from task_manager.mixins import AuthenticateMixin, DeleteProtectionMixin


class LabelsView(AuthenticateMixin, ListView):
    template_name = 'labels/list.html'
    model = Label
    context_object_name = 'labels'


class LabelCreateView(AuthenticateMixin, SuccessMessageMixin, CreateView):
    template_name = 'labels/create.html'
    model = Label
    form_class = LabelForm
    success_message = _('Label created successfully')
    success_url = reverse_lazy('labels_list')


class LabelUpdateView(AuthenticateMixin, SuccessMessageMixin, UpdateView):
    template_name = 'labels/update.html'
    model = Label
    form_class = LabelForm
    success_message = _('Label updated successfully')
    success_url = reverse_lazy('labels_list')


class LabelDeleteView(AuthenticateMixin, DeleteProtectionMixin,
                      SuccessMessageMixin, DeleteView):
    template_name = 'labels/delete.html'
    model = Label
    success_message = _('Label deleted successfully')
    success_url = reverse_lazy('labels_list')
    rejection_message = _('Unable to delete label because it is in use')
    rejection_url = reverse_lazy('labels_list')
