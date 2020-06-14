from django.db import models

# Create your models here.
from django.db.models import CharField

"""Model for ever Class of room"""


class Roomclass(models.Model):
    name = models.CharField(blank=False, max_length=40)
    unique_color = models.CharField(blank=True, max_length=15)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=False)

    def __str__(self):
        return self.name


"""This is a model for every single room"""


class Room(models.Model):
    ROOM_STATUS = (
        ('O', 'Occupied'),
        ('U', 'Unoccupied'),
        ('B', 'Booked')
    )
    ROOM_CONDITION = (
        ('G', 'Good'),
        ('B', 'Bad'),
        ('E', 'Excellent')
    )
    roomclass = models.ForeignKey(Roomclass, on_delete=models.CASCADE)
    room_no = models.IntegerField(blank=False)
    status = models.CharField(choices=ROOM_STATUS, blank=False, max_length=30)
    occupied = models.CharField(choices=ROOM_CONDITION, blank=False, max_length=30)

    def __str__(self):
        return str(self.room_no)
