from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.description

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    qty = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True, blank=True)
    thumbnail = models.CharField(max_length=255, null=True)
    images =  models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.name