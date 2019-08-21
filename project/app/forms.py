from django import forms
from django.forms import ModelForm
from .models import Login


class LoginForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Login
        fields = ['email','password']
