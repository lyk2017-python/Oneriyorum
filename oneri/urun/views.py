from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


from urun.forms import CommentForm, ContactForm, UserRegisterForm
from urun.models import Product, Vendor


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

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CommentCreate(CreateView):
    form_class = CommentForm
    template_name = "urun/comment_form.html"
    def get_form_kwargs(self):
        form_veri = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            kullanici_veri = form_veri["data"].copy()
            kullanici_veri["product"] = self.kwargs["pk"]
            form_veri["data"] = kullanici_veri
        return form_veri


class AnasayfaView(generic.ListView):
    model = Product

class SssView(generic.TemplateView):
    template_name = "urun/sss.html"

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
                ["sahinelif.mail@gmail.com"])
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