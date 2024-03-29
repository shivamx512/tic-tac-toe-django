from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Game


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User


class GamesForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"