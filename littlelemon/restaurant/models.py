from django.db import models

# Create your models here.


class Booking(models.Model):
    id = models.SmallIntegerField(default=11).primary_key
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=6)
    booking_date = models.DateField(db_index=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    id = models.SmallIntegerField(default=5).primary_key
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=5)

    def __str__(self):
        return self.title
