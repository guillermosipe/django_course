from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

from .forms import SignUpForm,ContactForm

from .models import SignUp

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

	if request.user.is_authenticated() and request.user.is_staff:
		#print(SignUp.objects.all())
		#i=1
		#for instance in SignUp.objects.all():
		#	print(i,instance.full_name)
		#	i += 1
		
		datos = SignUp.objects.all().order_by('-timestamp')#.filter(full_name__icontains='guillermo')
		context = {
			"datos" : datos
		}
	

	return render(request,"home.html",context)


def contact(request):
	title = "Contacto"
	form = ContactForm(request.POST or None)
	title_align_center = True

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
		"form" : form,
		"title" : title,
		"title_align_center":title_align_center
	}

	return render(request,"forms.html",context)
