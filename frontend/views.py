from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from storageapp.models import file_uploader, image
from .forms import file_Upload_form, image_Upload_form

from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required
def upload_file(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = file_Upload_form(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_id =user.id
            form.save()
            messages.success(request, f"file upload successful!")
            return redirect('home')
    
    else:
        form = file_Upload_form()
    return render(request, 'uploadfile.html', {'form': form})


@login_required
def my_files(request):
    files = file_uploader.objects.filter(user = request.user.id)
    return render(request, 'myfiles.html', {'files': files})


@login_required
def my_images(request):
    images = image.objects.filter(user = request.user.id)
    return render(request, 'myimages.html', {'images': images})



@login_required
def upload_image(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = image_Upload_form(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user_id =user.id
            form.save()
            messages.success(request, f"image upload successful!")
            return redirect('home')
    
    else:
        form = image_Upload_form()
    return render(request, 'uploadimage.html', {'form': form})
