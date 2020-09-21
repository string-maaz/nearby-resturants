from django.forms import ModelForm, Form
from django.contrib.auth import get_user_model
from django import forms


class LoginForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = get_user_model()
		fields = ['username','password']
	
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update(
		    {
		        'placeholder': 'Username',
		        'class': 'form-control'
		    })
		self.fields['password'].widget.attrs.update(
		    {
		        'placeholder': 'Password',
		        'class': 'form-control'
		    })

	def clean_username(self):
		if self.errors.get('username'):
			del self.errors['username']
		return self.data['username']