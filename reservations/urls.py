from django.contrib import admin
from django.urls import path
from .views import ReservationView, ContactView, MenuView, ReviewView, leave_review, make_reservation, list_reservations, update_reservation

urlpatterns = [
    path("contact_us/", ContactView.as_view(), name="contact"),
    path("leave_a_review/", ReviewView.as_view(), name="reviewView"),
    path("make_reservation/", make_reservation, name="reservationForm"),
    path("our_menu/", MenuView.as_view(), name="menu"),
    path("reservation/", ReservationView.as_view(), name="reservation"),
    # path("remove_reservation/<int:reservation_id>/", RemoveReservationView.as_view(), name="reservationRemove"),
    path("submit_review/", leave_review, name="submit_review"),
    path("update_reservation/<int:reservation_id>/", update_reservation, name="reservationUpdate"),
    path("your_reservation_details/", list_reservations, name="reservationDetails"),

]
