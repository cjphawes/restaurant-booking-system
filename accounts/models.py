from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=[("Customer", "Customer"), ("Admin", "Admin"), ("Member", "Member")])


def __str__(self):
    return self.user_id