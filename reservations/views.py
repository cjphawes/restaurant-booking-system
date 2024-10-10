from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from .models import Review, Reservation, User
from datetime import datetime

# Create your views here.
class ReservationView(TemplateView):
    template_name = 'reservations/reservations.html'


class ReservationDetailsView(TemplateView):
    template_name = 'reservations/view_reservation.html'


class ContactView(TemplateView):
    template_name = 'reservations/contact.html'


class MenuView(TemplateView):
    template_name = 'reservations/menu.html'


class ReviewView(TemplateView):
    template_name = 'reservations/review.html'

"""
Function to POST review forms to the database
"""
def leave_review(request):    
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        content = request.POST.get("content")

        if not name or not subject or not content:
            messages.error(request, "Please complete all fields.")
        else:
            review = Review(reviewer_name=name, subject=subject, review_content=content)

            review.save()
            messages.success(request, "Review submitted! Thank you for your feedback.")

        return render(request, "reservations/review.html", {'messages': messages.get_messages(request)})

    return render(request, "reservations/review.html")

def make_reservation(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        guests = request.POST.get("num_of_guests")
        time = request.POST.get("time")
        date = request.POST.get("date")

        if not name or not email or not date or not time or not guests:
            messages.error(request, "Please complete all fields.")
        else:
            """
            The datetime module I used to convert the string time into an object which works with Django's TimeField.
            """
            time_selected = datetime.strptime(time, '%H:%M').time()

            reservation = Reservation(email_address=email, name=name, reservation_date=date, reservation_time=time_selected, number_of_guests=guests)

            reservation.save()
            messages.success(request, "You're all set! We look forward to you joining us.")

        return render(request, "reservations/reservations.html", {'messages': messages.get_messages(request)})

    return render(request, "reservations/reservations.html")
