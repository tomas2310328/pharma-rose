from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .utils import unique_slug_generator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        related_name="children", 
        blank=True, null=True
    )


    def __str__(self):
        return self.name

        

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="products", blank=True)
    category = models.ForeignKey(
        Category, 
        related_name='categories', 
        on_delete=models.CASCADE, 
        blank=True, null=True
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("products:detail", kwargs={"slug":self.slug})



# Slug signals
@receiver(pre_save, sender=Product)
def product_slug_automaticaly(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Category)
def category_slug_automaticaly(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
