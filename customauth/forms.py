from django.contrib.auth.forms import (UserCreationForm, UsernameField,
                                       AuthenticationForm)
from customauth.models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username",)
        field_classes = {'username': UsernameField}


class LoginForm(AuthenticationForm):
    pass