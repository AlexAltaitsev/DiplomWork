from django import forms
from django.contrib.auth.models import User 


def unique_username(value):
    if User.objects.filter(username=value):
        raise forms.ValidationError("Username mast be unique")


class UserSigupForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100, validators=[unique_username])
    password = forms.CharField(label='Your password', max_length=100)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Your password', max_length=100)