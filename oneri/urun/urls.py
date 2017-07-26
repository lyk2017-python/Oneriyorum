from django.conf.urls import url
from . views import ProductView,

urlpatterns=[
    url(r"^$", AnasayfaView.as_view(), name="Anasayfa"),
    url(r"^product/(?P<pk>\d+)$", ProductView.as_view()),
    url(r"sss$", SSSView.as_view())
]