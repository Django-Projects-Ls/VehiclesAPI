from django.db import models


class Vehicle(models.Model):
    """This class represents the vehicle table."""

    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    speed = models.IntegerField()
    passengers = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name} - {self.model} - {self.year}"
