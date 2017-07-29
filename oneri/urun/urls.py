from django.conf.urls import url
from oneri.views import ProductDetailView, AnasayfaView, SssView, CommentCreate
from oneri.views import ProductCreate, ProductUpdate

urlpatterns=[
    url(r"^$", AnasayfaView.as_view(), name="Anasayfa"),
    url(r"^product/(?P<pk>\d+)$", ProductDetailView.as_view(), name="product"),
    url(r"sss$", SssView.as_view()),
    url(r'product/add/$', ProductCreate.as_view(), name='product-add'),
    url(r'product/update/(?P<pk>[0-9]+)/$', ProductUpdate.as_view(), name='product-update'),
    url(r'comment/add/', CommentCreate.as_view(), name='comment-add'),
]