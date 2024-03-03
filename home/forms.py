from django import forms
from django.forms import TextInput, Textarea

from .models import ContactModel


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = 'name', 'email', 'subject', 'messages'
        widgets: dict = {
            'name': TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "name", 'placeholder': "Your Name",
                       'required': "required",
                       'data-validation-required-message ': "Please enter your name"}),
            'email': TextInput(
                attrs={'type': 'email', 'class': "form-control", 'id': "email", 'placeholder': "Your Email",
                       'required': "required", 'data-validation-required-message': "Please enter your email"}),
            'subject': TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "subject", 'placeholder': "Subject",
                       'required': "required", 'data-validation-required-message': "Please enter a subject"}),
            'messages': Textarea(attrs={'class': "form-control", 'rows': "6", 'id': "message", 'placeholder': "Message",
                                       'required': "required",
                                       'data-validation-required-message': "Please enter your message"}),
            }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, widget=forms.TextInput())

