from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import ImageClient
from PIL import Image, ImageOps

# Create your views here.
def index(request):
    return render(request, 'img/index.html')

def new(request):
    """
    Returns mirror image from client.
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.open(form.cleaned_data['image'])
            form.image = ImageOps.mirror(image)
            form.save()
            return redirect('img:index')
    else:
        form = ImageForm()
    return render(request, 'img/new_egami.html', {'form':form})


def detail(request, pk):
    image = get_object_or_404(ImageClient, pk=pk)
    return render(request, 'img/egami_detail.html', {'image':image})