from django.conf.urls import url

from urun.views import ProductDetailView, AnasayfaView, CommentCreate, ContactFormView, UserRegisterView, like, \
    dislike, comment_like, comment_dislike
from urun.views import ProductCreate, ProductUpdate, ProductDelete, VendorCreate, ProductListSearchView

urlpatterns=[
    url(r"^$", AnasayfaView.as_view(), name="Anasayfa"),
    url(r'^vendor/add/$', VendorCreate.as_view(), name='vendor-add'),
    url(r'^product/add/$', ProductCreate.as_view(), name='product-add'),
    url(r'^contact/$', ContactFormView.as_view(), name='contact'),
    url(r"^product/(?P<pk>\d+)/$", ProductDetailView.as_view(), name="product-detail"),
    url(r'^product/(?P<pk>\d+)/add/', CommentCreate.as_view(), name='comment-add'),
    url(r'^product/(?P<pk>\d+)/update/$', ProductUpdate.as_view(), name='product-update'),
    url(r'^product/(?P<pk>\d+)/delete/$', ProductDelete.as_view(), name='product-delete'),
    url(r'^product/search/', ProductListSearchView.as_view(), name='product-list-search'),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
    url(r"^api/like$", like, name="like_dislike"),
    url(r"^api/dislike$", dislike, name="dislike"),
    url(r"^api/comment_like$", comment_like, name="comment_like"),
    url(r"^api/comment_dislike$", comment_dislike, name="comment_dislike"),
]