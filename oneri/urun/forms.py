from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Comment, Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['vendor', 'name', 'description', 'image', 'price', 'performance', 'design', 'created_by']
        widgets = {"created_by": forms.HiddenInput()}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content', 'product']
        widgets = {"product": forms.HiddenInput()}

class ContactForm(forms.Form):

    email = forms.EmailField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()