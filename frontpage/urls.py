from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = "home-frontpage"), 
	path('contact.html', views.contact, name = "contact-frontpage"),
	path('about.html', views.about, name = "about-frontpage"),
	path('pricing.html', views.pricing, name = "pricing-frontpage"),
	path('service.html', views.service, name = "service-frontpage"),
	path('appointment.html', views.appointment, name = "appointment-frontpage") 
]
