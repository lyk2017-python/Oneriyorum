from django.db import models

class Vendor(models.Model):
    """
    This class is written for Product's vendor.
    """
    name = models.CharField(max_length=200)

    # This function return vendor's name.
    def __str__(self):
        return "{name}".format(name=self.name)


class Product(models.Model):
    """This class is written for user's comments. The comments have to include an image"""
    vendor = models.ManyToManyField("Vendor")
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    price = models.SmallIntegerField()
    performance = models.SmallIntegerField()
    design = models.SmallIntegerField(default=0)

    #    #This function return product's name.
    def __str__(self):
        return "{name}".format(name=self.name)

class Comment(models.Model):
    """
    This class is written for user's comments. The comments have to include an image
    """
    product = models.ForeignKey('Product', related_name="comments")
    content = models.TextField()
    like = models.IntegerField()
    dislike = models.IntegerField()


    def __str__(self):
        return "{name}".format(name=self.product)