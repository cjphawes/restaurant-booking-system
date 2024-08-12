from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Customer(models.Model):
#     customer_id = models.AutoField(primary_key=True)
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email_address = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15)


# def __str__(self):
#     return self.customer_id


# class Table(models.Model):
#     table_id = models.AutoField(primary_key=True)
#     reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
#     table_number = models.IntegerField(unique=True)


# def __str__(self):
#     return self.table_id


# class Reservation(models.Model):
#     reservation_id = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     table = models.ForeignKey(Table, on_delete=models.CASCADE)
#     reservation_time = models.TimeField()
#     reservation_date = models.DateField()
#     num_of_guests = models.IntegerField()


# def __str__(self):
#     return self.reservation_id


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=100)
#     role = models.CharField(max_length=20, choices=[("Customer", "Customer"), ("Admin", "Admin"), ("Member", "Member")])


# def __str__(self):
#     return self.user_id