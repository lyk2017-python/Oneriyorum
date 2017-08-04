from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin


from urun.forms import CommentForm, ContactForm, UserRegisterForm
from urun.models import Product, Vendor, Comment


class LoginCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class LoginUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass


class LoginDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass


class VendorCreate(LoginCreateView):
    model = Vendor
    fields = ['name']


class ProductCreate(LoginCreateView):
    model = Product
    fields = ['vendor', 'name', 'description', 'image', 'price', 'performance', 'design']


class ProductUpdate(LoginUpdateView):
    model = Product
    fields = ['vendor', 'name', 'description', 'image', 'price', 'performance', 'design']
    template_name = 'urun/product_form_update.html'


class ProductDelete(LoginDeleteView):
    model = Product
    success_url = reverse_lazy('Anasayfa')
    template_name = 'urun/product_form_delete.html'

    """Ilgili product pk'sina erisim icin get komutu """
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CommentCreate(CreateView):
    form_class = CommentForm
    template_name = "urun/comment_form.html"

    """ Yorum yapilcak urunun pk'sina ulasabilmek icin kullanilan fonksiyon """
    def get_form_kwargs(self):
        """ Form verilerini kaybetmemek icin super kullaniyoruz."""
        form_veri = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:

            """ Data kullanici_veri'ye kopyalaniyor """
            kullanici_veri = form_veri["data"].copy()

            """Kullanici_veriye ppk ekleniyor"""
            kullanici_veri["product"] = self.kwargs["pk"]

            """Form_veriye geri aktariliyor."""
            form_veri["data"] = kullanici_veri
        return form_veri


class AnasayfaView(generic.ListView):
    model = Product
    ordering = ['-pk']


class ProductDetailView(generic.DetailView):
    model = Product

class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "urun/contact.html"
    success_url = "/"

    def form_valid(self, form):
        data = form.cleaned_data
        from django.conf import settings
        send_mail("Oneriyorum ContactForm : {}".format(data["title"]),
                "Sistemden size gelen bir mesaj var\n---\n{}\n---\neposta: {}\nip: {}".format(data["content"], data["email"], self.request.META["REMOTE_ADDR"]),
                settings.DEFAULT_FROM_EMAIL,
                ["info@oneriyorum.com"])
        return super().form_valid(form)

class ProductListSearchView(AnasayfaView):
    paginate_by = 10

    def get_queryset(self):
        result = super(AnasayfaView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:

            result = result.filter(name__icontains=query)

        return result



class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = "urun/signup.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def like(request):
    id = request.POST.get("id", default=None)
    like = request.POST.get("like")
    obj = get_object_or_404(Product, id=int(id))
    if like == "true":
        obj.like = F("like") + 1
        obj.save(update_fields=["like"])
    else:
        return HttpResponse(status=400)
    obj.refresh_from_db()
    return JsonResponse({"like": obj.like, "id": id})

def dislike(request):
    id = request.POST.get("id", default=None)
    dislike = request.POST.get("dislike")
    obj = get_object_or_404(Product, id=int(id))
    if dislike == "true":
        obj.dislike = F("dislike") + 1
        obj.save(update_fields=["dislike"])
    else:
        return HttpResponse(status=400)
    obj.refresh_from_db()
    return JsonResponse({"dislike": obj.dislike, "id": id})

def comment_like(request):
    id = request.POST.get("id", default=None)
    like = request.POST.get("like")
    obj = get_object_or_404(Comment, id=int(id))
    if like == "true":
        obj.like = F("like") + 1
        obj.save(update_fields=["like"])
    else:
        return HttpResponse(status=400)
    obj.refresh_from_db()
    return JsonResponse({"like": obj.like, "id": id})

def comment_dislike(request):
    id = request.POST.get("id", default=None)
    dislike = request.POST.get("dislike")
    obj = get_object_or_404(Comment, id=int(id))
    if dislike == "true":
        obj.dislike = F("dislike") + 1
        obj.save(update_fields=["dislike"])
    else:
        return HttpResponse(status=400)
    obj.refresh_from_db()
    return JsonResponse({"dislike": obj.dislike, "id": id})