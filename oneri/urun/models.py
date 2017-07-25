from django.db import models


class Product(models.Model):
    customer = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    comment = models.TextField()
    image = models.ImageField()
    score = models.SmallIntegerField()
    price = models.SmallIntegerField
    performance = models.SmallIntegerField()
    design = models.SmallIntegerField()

    def __str__(self):
        return self.name
# Create your models here.
