from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()
    email = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','password']

class LoginForm(forms.Form):
    username1 = forms.CharField(max_length=50)
    password1=forms.CharField(widget=forms.PasswordInput)
    email1 = forms.CharField(max_length=90)