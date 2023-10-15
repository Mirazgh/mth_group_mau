from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class regform(UserCreationForm):
    id_number = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'id_number', 'password1', 'password2']

class login_form(forms.Form):
    username = forms.CharField(max_length=150)
