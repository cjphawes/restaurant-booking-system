from django.contrib import admin
from .models import Customer, Reservation, Table

# Register your models here.
admin.site.register(Customer)
admin.site.register(Reservation)
admin.site.register(Table)