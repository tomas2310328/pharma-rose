from django.db import models

# Create your models here.



class Checking(models.Model):
    bar_code        = models.CharField(max_length=50)
    serial_number   = models.CharField(max_length=50)

    def __str__(self):
        return str(self.serial_number)
