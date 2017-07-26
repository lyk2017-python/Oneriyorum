from django.conf.urls import url
from oneri.views import ProductDetailView, AnasayfaView, SssView

urlpatterns=[
    url(r"^$", AnasayfaView.as_view(), name="Anasayfa"),
    url(r"^product/(?P<pk>\d+)$", ProductDetailView.as_view()),
    url(r"sss$", SssView.as_view())
]