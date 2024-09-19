from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Review, Reservation, Customer, User

# Create your views here.
class ReservationView(TemplateView):
    template_name = 'reservations/booking.html'


class ContactView(TemplateView):
    template_name = 'reservations/contact.html'


class MenuView(TemplateView):
    template_name = 'reservations/menu.html'


def review_form(request):
    if request.method =='POST':
        reviewer_email = request.POST.get('reviewer_email')
        reviewer_name = request.POST.get('reviewer_name')
        subject = request.POST.get('subject')
        review_date = request.POST.get('review_date')
        review_content = request.POST.get('review_content')



    return render(request,)