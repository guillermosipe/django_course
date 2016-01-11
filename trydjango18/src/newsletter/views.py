from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

from .forms import SignUpForm,ContactForm
# Create your views here.
def home(request):
	title = "Bienvenido"
	form = SignUpForm(request.POST or None)
	context = {
		"title" : title,
		"form" : form
	}

	if form.is_valid():
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "Nuevo full_name"
		instance.full_name = full_name

		instance.save()

		context = {
			"title" : "Registro exitoso"
		}
	

	return render(request,"home.html",context)


def contact(request):
	form = ContactForm(request.POST or None)

	if form.is_valid():
		#for key in form.cleaned_data:
		#	print (key,form.cleaned_data.get(key))
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")

		contact_message = "%s: %s via %s"%(form_full_name,form_message,form_email)

		subject = "Test send django"
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_email]
		send_mail(subject,
				  contact_message,
				  from_email,
				  to_email,
				  fail_silently=False)


	context = {
		"form" : form
	}

	return render(request,"forms.html",context)
