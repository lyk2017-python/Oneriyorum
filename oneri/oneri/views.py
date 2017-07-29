from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from urun.models import Product, Vendor, Comment

class ProductCreate(CreateView):
    model = Product
    fields = ['vendor', 'name', 'description', 'image', 'price', 'performance', 'design']



class AnasayfaView(generic.ListView):
    model = Product

class SssView(generic.TemplateView):
    template_name = "urun/sss.html"

class ProductDetailView(generic.DetailView):
    model = Product



