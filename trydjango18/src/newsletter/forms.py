from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base,provider = email.split('@')
		domain,extension = provider.split('.')
		if not domain == 'ipn':
			raise forms.ValidationError("Agrege un dominio del IPN.")
		if not extension == 'mx':
			raise forms.ValidationError("El correo debe de ser de México.")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()