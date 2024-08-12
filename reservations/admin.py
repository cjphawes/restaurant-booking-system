from django.contrib import admin
from .models import Customer, Reservation
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):  
    list_display = ('customer', 'reservation_id', 'reservation_date')
    search_fields = (['customer'])
    list_filter = ('customer', 'reservation_date',)
    

# Register your models here.
admin.site.register(Customer)
