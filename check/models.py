from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from products.models import Product
from .utils import generate_key

class Checking(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name="products", 
        blank=True, null=True
    )
    bar_code        = models.CharField(max_length=50, unique=True)
    serial_number   = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.serial_number)


@receiver(post_save, sender=Product)
def create_checking_for_product(sender, instance, *args, **kwargs):
    check = Checking.objects.filter(product=instance)
    difference = abs(check.count() - instance.quantity)
    if instance and instance.quantity and difference > 0:
        for _ in range(difference):
            Checking.objects.create(
                product=instance, 
                bar_code=generate_key(5), 
                serial_number=generate_key(7)
            )
