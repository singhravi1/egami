from django import forms
from .models import Image_client

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image_client
        fields = ('image')
