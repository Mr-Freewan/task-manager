from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

from .models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=150,
                                 required=True,
                                 label=_("First name"))
    last_name = forms.CharField(max_length=150,
                                required=True,
                                label=_("Last name"))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2')


class UpdateUserForm(UserForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username
