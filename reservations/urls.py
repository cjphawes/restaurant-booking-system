from django.contrib import admin
from django.urls import path
from .views import ReservationView, ContactView, MenuView, ReviewView, ReservationDetailsView, leave_review, make_reservation, RemoveReservationView, UpdateReservationView, list_reservations

urlpatterns = [
    path("reservation/", ReservationView.as_view(), name="reservation"),
    path("your_reservation_details/", ReservationDetailsView.as_view(), name="reservationDetails"),
    path("contact_us/", ContactView.as_view(), name="contact"),
    path("leave_a_review/", ReviewView.as_view(), name="reviewView"),
    path("our_menu/", MenuView.as_view(), name="menu"),
    path("submit_review/", leave_review, name="submit_review"),
    path("make_reservation/", make_reservation, name="reservationForm"),
    path("remove_reservation/", RemoveReservationView.as_view(), name="reservationRemove"),
    path("update_reservation/", UpdateReservationView.as_view(), name="reservationUpdate"),
    path("your_reservations/", list_reservations, name="reservationInfo"),

]
