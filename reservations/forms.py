from django import forms
from .models import Reservation


# class ReservationForm(forms.ModelForm):
#     class Meta:
#         model = Reservation
#         fields = '__all__'
#         widgets = {
#             'customer': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'title': 'max_length=100',
#                     'placeholder': 'Name',
#                 }
#             ),
#             'reservation_time': forms.TimeInput(
#                 attrs={
#                     'class': 'form-control',
#                     'title': ''
#                 }
#             )
#         }