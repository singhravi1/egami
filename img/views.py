from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import ImageClient
from PIL import Image, ImageOps
import stripe

# Create your views here.
def index(request):
    return render(request, 'img/index.html')

def new(request):
    """
    Returns mirror image from client.
    """
    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            image = Image.open(form.image)
            image = ImageOps.mirror(image)
            form.image = image
            form.save()
            return redirect('img:detail', slug=form.id)
    else:
        form = ImageForm()
    return render(request, 'img/new_egami.html', {'form':form})


def detail(request, slug=None):
    image = get_object_or_404(ImageClient, slug=slug)
    return render(request, 'img/egami_detail.html', {'image':image})