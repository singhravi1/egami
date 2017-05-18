from django import forms
from .models import ImageClient

class ImageForm(forms.ModelForm):
	class Meta:
		model = ImageClient
		fields =('image',)