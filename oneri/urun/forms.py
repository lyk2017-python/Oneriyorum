from django import forms

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
