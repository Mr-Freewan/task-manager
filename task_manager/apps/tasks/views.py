from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView

from task_manager.apps.tasks.filters import TaskFilter
from task_manager.apps.tasks.forms import TaskForm
from task_manager.apps.tasks.models import Task
from task_manager.apps.users.models import User
from task_manager.mixins import AuthenticateMixin, AuthorPermissionMixin


class TasksView(AuthenticateMixin, FilterView):
    template_name = 'tasks/list.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'


class TaskInfoView(AuthenticateMixin, DetailView):
    template_name = 'tasks/task_info.html'
    model = Task
    context_object_name = 'task'


class TaskCreateView(AuthenticateMixin, SuccessMessageMixin, CreateView):
    template_name = 'tasks/create.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task created successfully')

    def form_valid(self, form):
        form.instance.author = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


class TaskUpdateView(AuthenticateMixin, SuccessMessageMixin, UpdateView):
    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task updated successfully')


class TaskDeleteView(AuthenticateMixin, AuthorPermissionMixin,
                     SuccessMessageMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks_list')
    success_message = _('Task deleted successfully')
    author_permission_message = _('Only the author of the task can delete it')
    author_permission_url = reverse_lazy('tasks_list')
