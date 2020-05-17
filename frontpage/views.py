from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
	return render(request, 'home.html',{})

def contact(request):
	if request.method == 'POST':
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			'TITLE Try add some info -- '+ message_name, # subject
			message, # message
			message_email, # from email
			['fakesanges@gmail.com','jogh@gmail.com'] # To Email

			)

		return render(request, 'contact.html',{'message_name': message_name})
	else:
		return render(request, 'contact.html',{})

def appointment(request):
	
	if request.method == 'POST':
		
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']
		# send an email
		appointment = "Name: " + your_name + "Schedule: " + your_schedule

		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_message, # from email
			['fakesanges@gmail.com','jogh@gmail.com'] # To Email

			)
		
		return render(request, 'appointment.html',{'your_schedule': your_schedule,
			'your_name': your_name})
	else:
		return render(request, 'home.html',{})

def about(request):
	return render(request, 'about.html',{})
def pricing(request):
	return render(request, 'pricing.html',{})
def service(request):
	return render(request, 'service.html',{})