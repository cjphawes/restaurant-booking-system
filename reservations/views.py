from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.
class ReservationView(TemplateView):
    template_name = 'reservations/booking.html'


class ContactView(TemplateView):
    template_name = 'reservations/contact.html'


class MenuView(TemplateView):
    template_name = 'reservations/menu.html'
