from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    """
    Function to display the parameters in the admin panel for a Customer
    """
    def __str__(self):
        return f"{self.full_name}"


TIME_PERIODS = (
    (0, '17:00'),
    (1, '17:30'),
    (2, '18:00'),
    (3, '18:30'),
    (4, '19:00'),
    (5, '19:30'),
    (6, '20:00'),
    (7, '20:30'),
    (8, '21:00'),
    (9, '21:30'),
    (10, '22:00'),
    (11, '22:30'),
    (12, '23:00'),
)


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="client_name")
    reservation_time = models.IntegerField(choices=TIME_PERIODS, default=0)
    reservation_date = models.DateField()
    number_of_guests = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])

    class Meta:
        ordering = ["reservation_date"]

    """
    Function to display the parameters in the admin panel for a Reservation
    """
    def __str__(self):
        return f"Reservation for {self.number_of_guests} at {self.reservation_time} on {self.reservation_date} for {self.customer}"


class Review(models.Model):
    reviewer_email = models.EmailField(unique=True)
    reviewer_name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    review_date = models.DateField()
    review_content = models.TextField()

    class Meta:
        ordering = ["review_date"]

    """
    Function to display the parameters in the admin panel for the reviews
    """
    def __str__(self):
        return f"{self.reviewer_name} sent a review about '{self.subject}'"