from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Customer(User):
    """Customer model
    for creating customer instance in database
    """
    phone = models.CharField(max_length=20, default=None)
    User._meta.get_field('email')._unique = True

    def get_absolute_url(self: User) -> reverse:
        """function for getting absolute url for individual customer objects
        """
        return reverse('users:customer_detail', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     super(Customer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'


class DeliveryAgent(User):
    phone = models.CharField(max_length=20)
    User._meta.get_field('email')._unique = True

    # def save(self, *args, **kwargs):
    #     super(DeliveryAgent, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'delivery agent'
        verbose_name_plural = 'delivery Agents'
