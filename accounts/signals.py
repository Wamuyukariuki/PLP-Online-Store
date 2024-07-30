from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer, Vendor

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Automatically create a Customer profile for every new user
        Customer.objects.create(user=instance)

        # Uncomment the following line if you want to create a Vendor profile instead
        # Vendor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.customer.save()
    # Uncomment the following line if you want to save the Vendor profile instead
    # instance.vendor.save()
