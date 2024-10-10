from django.contrib import admin
from django.urls import path
from .views import ReservationView, ContactView, MenuView, ReviewView, leave_review, make_reservation, RemoveReservationView, UpdateReservationView, list_reservations

urlpatterns = [
    path("contact_us/", ContactView.as_view(), name="contact"),
    path("leave_a_review/", ReviewView.as_view(), name="reviewView"),
    path("make_reservation/", make_reservation, name="reservationForm"),
    path("our_menu/", MenuView.as_view(), name="menu"),
    path("reservation/", ReservationView.as_view(), name="reservation"),
    path("remove_reservation/<int:id>/", RemoveReservationView.as_view(), name="reservationRemove"),
    path("submit_review/", leave_review, name="submit_review"),
    path("update_reservation/<int:id>/", UpdateReservationView.as_view(), name="reservationUpdate"),
    path("your_reservation_details/", list_reservations, name="reservationDetails"),

]
