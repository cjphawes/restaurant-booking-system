from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Reservation(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client_name")
    name = models.CharField(max_length=150)
    reservation_time = models.TimeField()
    reservation_date = models.DateField()
    number_of_guests = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        ordering = ["reservation_date"]

    """
    Function to display the parameters in the admin panel for a Reservation
    """
    def __str__(self):
        return f"""
        Reservation for {self.number_of_guests} at {self.reservation_time}
        on {self.reservation_date} for {self.customer}"""


class Review(models.Model):
    reviewer_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=250)
    review_date = models.DateTimeField(auto_now_add=True)
    review_content = models.TextField()

    class Meta:
        ordering = ["review_date"]

    """
    Function to display the parameters in the admin panel for the reviews
    """
    def __str__(self):
        return f"{self.reviewer_name} sent a review about '{self.subject}'"
