from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.Textarea()

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == name.lower():
            raise ValidationError('Sorry! name must be lowercase.')

        return name