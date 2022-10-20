from django.db import models

# Create your models here.


class Ticket(models.Model):

    id = models.IntegerField(primary_key=True)
    printer_model = models.CharField(max_length=20)
    toner_color = models.CharField(max_length=10)
    location = models.CharField(max_length=200)
    requested_by = models.CharField(max_length=50)

    def __repr__(self):
        return f"<Ticket ({self.id},{self.toner_color})>"

    def __str__(self):
        return self.__repr__()
