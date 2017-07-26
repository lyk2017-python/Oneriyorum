from django.contrib import admin

from .models import Product, Vendor, Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "performance", "design"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor)
admin.site.register(Comment)

