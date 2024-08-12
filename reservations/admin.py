from django.contrib import admin
from .models import Customer, Reservation
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):  
    list_display = ('customer', 'reservation_id', 'reservation_date')
    search_fields = (['customer__full_name__icontains', 'reservation_date'])
    list_filter = ('customer', 'reservation_date',)
    

@admin.register(Customer)
class CustomerAdmin(SummernoteModelAdmin):  
    list_display = ('full_name', 'email_address')
    search_fields = (['full_name'])
    list_filter = ('full_name',)
