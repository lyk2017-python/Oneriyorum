from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from urun.models import Product, Vendor, Comment

class ProductCreate(CreateView):
    model = Product
    fields = ['vendor', 'name', 'description', 'image', 'price', 'performance', 'design']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['vendor', 'name', 'description', 'image', 'price', 'performance', 'design']
    template_name = 'urun/product_form_update.html'

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('author-list')

class CommentCreate(CreateView):
    model = Comment
    fields = ['product', 'content']


class AnasayfaView(generic.ListView):
    model = Product

class SssView(generic.TemplateView):
    template_name = "urun/sss.html"

class ProductDetailView(generic.DetailView):
    model = Product



