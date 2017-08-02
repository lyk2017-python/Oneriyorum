from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content', 'product']
        widgets = {"product": forms.HiddenInput()}

class ContactForm(forms.Form):

    email = forms.EmailField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)


class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()