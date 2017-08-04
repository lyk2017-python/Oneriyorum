from django.db import models
from django.utils import timezone
from django.urls import reverse

class Vendor(models.Model):
    """
    This class is written for Product's vendor.
    """
    name = models.CharField(max_length=200)

    # This function return vendor's name.
    def __str__(self):
        return "{name}".format(name=self.name)

    def get_absolute_url(self):
        return reverse('Anasayfa')


class Product(models.Model):
    """This class is written for user's comments. The comments have to include an image"""
    vendor = models.ManyToManyField("Vendor")
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    """ Secenekler icin aralık belirleniyor. """
    SCORE_CHOICES = [(int(i), str(i)) for i in range(1, 6)]
    """ choices ile secenekler ekleniyor """
    price = models.SmallIntegerField(choices=SCORE_CHOICES)
    performance = models.SmallIntegerField(choices=SCORE_CHOICES)
    design = models.SmallIntegerField(choices=SCORE_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)


    # This function return product's name.
    def __str__(self):
        return "{name}".format(name=self.name)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class Comment(models.Model):


    product = models.ForeignKey('Product', related_name="comments")
    content = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return "{name}".format(name=self.product)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.product.pk})