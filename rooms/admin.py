from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Room)
admin.site.register(models.RoomCategory)
admin.site.register(models.Invoice)
admin.site.register(models.Customer)