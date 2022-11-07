from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import BlogUser

class BlogUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label='Password',
        max_length=20,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm password',
        max_length=20,
    )

    class Meta:
        model = BlogUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class BlogUserChangeForm(UserChangeForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput,
        label='New password',
        max_length=20,
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm new password',
        max_length=20,
    )
    class Meta:
        model = BlogUser
        fields = [
            'photo',
            'new_password1',
            'new_password2',
        ]