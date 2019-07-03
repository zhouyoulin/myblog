from django import forms
from django.contrib.auth.models import User
from . import models

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(label='Confirm Password:', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] == cd['password2']:
            raise forms.ValidationError("password not match")
        return cd['password2']

class UserInfoForm(forms.Form):
    birth = forms.CharField()
    phone = forms.CharField()
