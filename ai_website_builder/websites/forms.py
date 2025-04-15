from django import forms
from .models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['title', 'content', 'layout']  # Adjust the fields as necessary
