from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse
from .models import Review, Reservation, User
from datetime import datetime


class ReservationView(TemplateView):
    template_name = 'reservations/reservations.html'


class ContactView(TemplateView):
    template_name = 'reservations/contact.html'


class MenuView(TemplateView):
    template_name = 'reservations/menu.html'


"""
Function display all of the users reservations made
"""


@login_required
def list_reservations(request):
    reservations = Reservation.objects.filter(customer=request.user)
    return render(request, 'reservations/view_reservation.html',
                  {'reservations': reservations})


"""
Function to allow user to update their reservation
"""


def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == "POST":
        reservation_date = request.POST.get("date")
        reservation_time = request.POST.get("time")
        number_of_guests = request.POST.get("num_of_guests")
        reservation.save()

        if not reservation_date or not reservation_time or not number_of_guests:
            messages.error(request, "Please complete all fields.")
        else:
            """
            The datetime module I used to convert the string time into an
            object which works with Django's TimeField.
            """
            time_selected = datetime.strptime(reservation_time, '%H:%M').time()

            reservation.reservation_date = reservation_date
            reservation.reservation_time = time_selected
            reservation.number_of_guests = number_of_guests
            reservation.save()

            messages.success(request, "Reservation updated successfully!")

            return redirect('reservationDetails')

    return render(request, "reservations/update_reservation.html",
                  {'reservation': reservation})


"""
Function to delete existing reservations
"""


def remove_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Reservation successfully deleted!")

        return redirect("reservationDetails")

    return render(request, 'reservations/delete_reservation.html',
                  {'reservation': reservation})


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
            review = Review(reviewer_name=name, subject=subject,
                            review_content=content)

            review.save()
            messages.success(request,
                             "Review submitted! Thank you for your feedback.")

        return redirect("contact")

    return render(request, "reservations/review.html")


"""
Function to create a reservation to the database
"""


def make_reservation(request):
    if request.method == "POST":
        name = request.POST.get("name")
        guests = request.POST.get("num_of_guests")
        time = request.POST.get("time")
        date = request.POST.get("date")

        if not name or not date or not time or not guests:
            messages.error(request, "Please complete all fields.")
        else:
            """
            The datetime module I used to convert the string time into an
            object which works with Django's TimeField.
            """
            time_selected = datetime.strptime(time, '%H:%M').time()

            reservation = Reservation(customer=request.user, name=name,
                                      reservation_date=date,
                                      reservation_time=time_selected,
                                      number_of_guests=guests)

            reservation.save()
            messages.success(request,
                             "You're all set! We look forward to you joining us.")

            client_email = reservation.customer.email
        return redirect('reservation')

    return render(request, "reservations/reservations.html")
