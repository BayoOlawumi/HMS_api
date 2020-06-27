from django.db import models


# Create your models here.
from HMS_api import settings


class RoomCategory(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    unique_color = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name


'''Many to one relationship One category to many Rooms, related name Rooms gives the
 relationship of RoomCategory with Rooms
 
'''


class Room(models.Model):
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, related_name='rooms')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rooms_created', on_delete=models.CASCADE)
    # Whenever, the RoomCategory is deleted, all the Rooms associated with it gets deleted, Hence,CASCADE
    number = models.DecimalField(max_digits=9, decimal_places=0, blank=False, unique=True)
    status = models.CharField(max_length=30, blank=False)
    condition = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return str(self.number)


"""Customer has one to many relationship with the invoices

"""


class Customer(models.Model):
    fullname = models.CharField(max_length=60, blank=False)
    address = models.CharField(max_length=200, blank=False)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, blank=False)
    email_address = models.EmailField(blank=False, unique=True)


    def __str__(self):
        return str(self.fullname)


'''Invoice has many to one relationship with Customer and room
 
'''


class Invoice(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_invoices')
    # for every invoice, there is a room, one room to plenty invoices
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    # for every customer,there is a customer,one customer to one or manny invoices
    date_issued = models.DateTimeField(auto_now_add=True, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    details = models.CharField(max_length=150, blank=False)

    """ Arranges the Invoices in deceasing order of date
   
    class Meta:
        ordering = ('-date-issued',)
    """

    def __str__(self):
        return self.details
