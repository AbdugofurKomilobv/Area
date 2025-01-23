from django import forms

from pages.models import ContactMe


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = '__all__'

