from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)