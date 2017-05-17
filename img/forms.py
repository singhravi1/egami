from django import forms
# from .models import ImageClient

class ImageForm(forms.Form):
	image = forms.FileField(
		label = 'Select a file',
		help_text= 'Jpg, jpeg only')