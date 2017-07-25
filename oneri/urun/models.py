from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    vendor = models.ManyToManyField("Vendor")
    name = models.CharField(max_length=200)
    image = models.ImageField()

class Comment(models.Model):

    vendor = models.ForeignKey('Product')
    comment = models.TextField()
    image = models.ImageField()
    price = models.SmallIntegerField()
    performance = models.SmallIntegerField()
    design = models.SmallIntegerField()

