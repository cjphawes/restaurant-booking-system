from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reservation_time = models.TimeField()
    reservation_date = models.DateField()
    number_of_guests = models.IntegerField(default=1)


    class Meta:
        ordering = ["-reservation_id"]


    def __str__(self):
        return f"Reservation for {self.number_of_guests} at {self.reservation_time} on {self.reservation_date} for {self.customer}"