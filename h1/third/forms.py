from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label = 'User Name', max_length=24)
	password = forms.CharField(widget = forms.PasswordInput())
