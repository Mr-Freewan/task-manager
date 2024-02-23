from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.models import Label


class LabelForm(forms.ModelForm):
    name = forms.CharField(max_length=155,
                           required=True,
                           label=_('Name'))

    class Meta:
        model = Label
        fields = ('name',)
