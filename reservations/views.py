from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from .models import Review, Reservation, Customer, User
from .forms import ReviewForm

# Create your views here.
class ReservationView(TemplateView):
    template_name = 'reservations/booking.html'


class ContactView(TemplateView):
    template_name = 'reservations/contact.html'


class FeedbackFormView(FormView):
    """
    Function to display form created in django
    """
    def review(request):
        if request.method =='POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = ReviewForm()
                
        return render(request, 'contact.html', {'review_form': form})


class MenuView(TemplateView):
    template_name = 'reservations/menu.html'