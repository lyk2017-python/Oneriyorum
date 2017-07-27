from django.contrib import admin

from .models import Product, Vendor, Comment


class ProductComment(admin.StackedInline):
    model = Comment
    extra = 0


class ProductAdmin(admin.ModelAdmin):

    list_display = ["name", "price", "performance", "design"]
    search_fields = ["name", "price"]
    list_filter = ["name", "price", "performance", "design"]
    inlines = [ProductComment]


#Derste yapılan diğerinden farkı yok sanırım
#@admin.register(Vendor)
#class VendorAdmin(admin.ModelAdmin):
#    pass



admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor)
admin.site.register(Comment)

