from django.contrib import admin

from .models import Product, Vendor, Comment

admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Comment)


