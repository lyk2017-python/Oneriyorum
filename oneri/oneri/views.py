from django.views import generic
from django.views.generic import ListView

from urun.models import Product, Vendor, Comment


class AnasayfaView(generic.ListView):
    model = Product

class SssView(generic.TemplateView):
    template_name = "urun/sss.html"

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "urun/product_detail2.html"



