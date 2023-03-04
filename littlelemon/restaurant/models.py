from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        default=0, verbose_name='Number of Guests')
    booking_date = models.DateTimeField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, db_index=True)
    booking_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
