from django.shortcuts import render

# Create your views here.
def index_reservation(request):
    return render(request, 'reservations/booking.html')


# class ReservationPage():
#     queryset = 
#     template_name = "reservations/booking.html"