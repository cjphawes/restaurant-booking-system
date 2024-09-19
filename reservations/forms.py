from django import forms
from .models import Reservation, Review


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['Number of guests', 'Date', 'Time',]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Email Address', 'Name', 'Subject', 'Review Content']