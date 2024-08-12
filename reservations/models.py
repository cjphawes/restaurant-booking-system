from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    """
    Function to display the parameters in the admin panel for a Customer
    """
    def __str__(self):
        return f"{self.full_name}"


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="client_name")
    reservation_time = models.TimeField()
    reservation_date = models.DateField()
    number_of_guests = models.IntegerField(default=1)


    class Meta:
        ordering = ["-reservation_id"]

    """
    Function to display the parameters in the admin panel for a Reservation
    """
    def __str__(self):
        return f"Reservation for {self.number_of_guests} at {self.reservation_time} on {self.reservation_date} for {self.customer}"