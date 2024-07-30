from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=50)  # e.g., 'Shipping' or 'Billing'
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address_type} - {self.street_address}, {self.city}"


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.business_name
