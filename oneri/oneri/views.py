from django.views import generic

from urun.models import Product


class AnasayfaView(generic.ListView):
    model = Product

class SssView(generic.TemplateView):
    template_name = "urun/sss.html"

class ProductDetailView(generic.DetailView):
    def get_queryset(self):
        return Product.objects.all()
