from django.db import models

class Vendor(models.Model):
    """This class is written for Product's vendor."""
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{name}".format(name=self.name)

class Product(models.Model):
    vendor = models.ManyToManyField("Vendor")
    name = models.CharField(max_length=200)
    image = models.ImageField(default=None, null=True)

class Comment(models.Model):
    """This class is written for user's comments. The comments have to include an image"""
    vendor = models.ForeignKey('Product')
    comment = models.TextField()
    image = models.ImageField(blank=True, null=True)
    price = models.SmallIntegerField()
    performance = models.SmallIntegerField()
    design = models.SmallIntegerField(default=0)

