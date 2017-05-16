from django.shortcuts import render
from .forms import ImageForm
from PIL import Image, ImageOps
import stripe

# Create your views here.
def egami(request):
    #TODO: Mirror image and then redirect download after paayement process
    pass
