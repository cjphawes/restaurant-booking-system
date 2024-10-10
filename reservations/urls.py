"""
URL configuration for kuidaore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import ReservationView, ContactView, MenuView, ReviewView, ReservationDetailsView, leave_review, make_reservation

urlpatterns = [
    path("reservation/", ReservationView.as_view(), name="reservation"),
    path("your_reservation_details/", ReservationDetailsView.as_view(), name="reservationDetails"),
    path("contact_us/", ContactView.as_view(), name="contact"),
    path("leave_a_review/", ReviewView.as_view(), name="reviewView"),
    path("our_menu/", MenuView.as_view(), name="menu"),
    path("submit_review/", leave_review, name="submit_review"),
    path("make_reservation/", make_reservation, name="reservationForm"),

]
