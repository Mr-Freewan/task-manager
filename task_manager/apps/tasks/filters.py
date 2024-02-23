import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _
from django_filters import ModelChoiceFilter

from task_manager.apps.tasks.models import Task
from task_manager.apps.labels.models import Label


class TaskFilter(django_filters.FilterSet):
    labels = ModelChoiceFilter(queryset=Label.objects.all(),
                               label=_('Label'))

    name = django_filters.BooleanFilter(field_name='author',
                                        widget=forms.CheckboxInput,
                                        label=_('Own tasks only'),
                                        method='get_own_tasks')

    def get_own_tasks(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(author=self.request.user)

    class Meta:
        model = Task
        fields = ['status', 'executor']
