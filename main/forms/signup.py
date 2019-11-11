from django.forms import Form
from django.forms.fields import EmailField, CharField
from django.forms.widgets import TextInput, PasswordInput, EmailInput

from main.models import User
from django.utils.translation import ugettext_lazy as _


class SignupForm(Form):
    first_name = CharField(
        max_length=255,
        required=True,
        widget=TextInput,
        label=_('First Name'))
    last_name = CharField(
        max_length=255,
        required=True,
        widget=TextInput,
        label=_('Last Name'))
    user_name = CharField(
        max_length=255,
        required=False,
        widget=TextInput,
        label=_('User Name'))
    email = EmailField(
        max_length=255,
        required=True,
        widget=EmailInput,
        label=_('E-mail Address'))
    password = CharField(
        min_length=8,
        max_length=255,
        required=True,
        widget=PasswordInput,
        label=_('Password'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    def create_user(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        user_name = self.cleaned_data.get('user_name')
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = None
        try:
            user = User.objects.create_user(
                email,
                password,
                first_name=first_name,
                last_name=last_name,
                user_name=user_name,)
        except:
            self.add_error(None, 'Error')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count() > 0:
            self.add_error('email', _('E-mail Address is already being used.'))
        return email
