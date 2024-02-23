from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.apps.statuses.models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(max_length=155,
                           required=True,
                           label=_('Name'))

    class Meta:
        model = Status
        fields = ('name',)
