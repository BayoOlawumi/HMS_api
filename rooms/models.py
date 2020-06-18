from django.db import models


# Create your models here.

class RoomCategory(models.Model):
    default_color = "#4354545"
    name = models.CharField(max_length=20, blank=False)
    unique_color = models.CharField(max_length=30, default=default_color, blank=False)

    """
    class Meta:
        ordering = ("name",)
        
    """

    def __str__(self):
        return self.name


'''Many to one relationship One category to many Rooms, related name Rooms gives the
 relationship of RoomCategory with Rooms
 
'''


class Room(models.Model):
    ROOM_STATUS = (
        ("O", "Occupied"),
        ("U", "Unoccupied"),
        ("B", "Booked"),
    )
    ROOM_CONDITION = (
        ("G", "Good"),
        ("B", "Bad"),
        ("E", "Excellent"),
    )

    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, related_name='rooms')
    # Whenever, the RoomCategory is deleted, all the Rooms associated with it gets deleted, Hence,CASCADE
    number = models.DecimalField(max_digits=9, decimal_places=0, blank=False, null=True)
    status = models.CharField(choices=ROOM_STATUS, max_length=10, blank=False, default="U"),
    condition = models.CharField(choices=ROOM_CONDITION, max_length=10, blank=False, default="G"),

    """
    
    class Meta:
        ordering = ('number',)
    """

    def __str__(self):
        return str(self.number)


"""Customer has one to many relationship with the invoices

"""


class Customer(models.Model):
    fullname = models.CharField(max_length=60, blank=False),
    address = models.CharField(max_length=200, blank=True),
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, blank=False),
    email_address = models.EmailField(blank=True),

    """
    class Meta:
        ordering = ('fullname_id',)
    """

    def __str__(self):
        return self.fullname


'''Invoice has many to one relationship with Customer and room
 
'''


class Invoice(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_invoices')
    # for every invoice, there is a room, one room to plenty invoices
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    # for every customer,there is a customer,one customer to one or manny invoices
    date_issued = models.DateTimeField(auto_now_add=True),
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False),
    details = models.CharField(max_length=150, blank=True)

    """ Arranges the Invoices in deceasing order of date
   
    class Meta:
        ordering = ('-date-issued',)
    """

    def __str__(self):
        return str(self.amount)
