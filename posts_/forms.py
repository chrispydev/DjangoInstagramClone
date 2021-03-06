from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'name': 'username', 'placeholder': 'username', }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'name': 'password', 'placeholder': 'password', }))
