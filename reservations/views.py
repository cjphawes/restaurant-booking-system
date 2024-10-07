from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from .models import Review, Reservation, User
from .forms import ReviewForm

# Create your views here.
class ReservationView(TemplateView):
    template_name = 'reservations/reservations.html'


class ContactView(TemplateView):
    template_name = 'reservations/contact.html'


class FeedbackFormView(FormView):
    """
    Function to display form created in django
    """
    template_name = 'reservations/review.html'
    form_class = ReviewForm
    
    def review(request):
        if request.method =='POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your review was successfully submitted, we thank you for your feedback!')
        else:
            form = ReviewForm()
                
        return render(request, 'review.html', {'review_form': form})


class MenuView(TemplateView):
    template_name = 'reservations/menu.html'