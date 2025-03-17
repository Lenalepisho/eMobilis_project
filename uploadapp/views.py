from django.core.files.storage import FileSystemStorage
from .models import UploadImage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# View for successful upload
def upload_success(request):
    return render(request, 'uploading/upload_success.html')


@login_required
def upload_image(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You need to be logged in to upload images.")
    #Continue with upload logic

# View for uploading images
@login_required  # Ensures only authenticated users can access
def upload_image(request):
    if not request.user.is_superuser:
        # Restrict access for non-superusers
        return HttpResponseForbidden("You do not have permission to upload images.")
    
    if request.method == 'POST':
        # Retrieve data from form
        title = request.POST.get('title')  # Use .get() to avoid KeyError
        upload_file = request.FILES.get('image')  # Access file from request.FILES

        if upload_file:
            # Save the file using FileSystemStorage
            fs = FileSystemStorage()
            filename = fs.save(upload_file.name, upload_file)
            file_url = fs.url(filename)

            # Save file information to the database
            image = UploadImage.objects.create(title=title, image=filename)
            image.save()

            return render(request, 'uploading/upload_success.html', {'file_url': file_url})

        # If no file is uploaded, return an error
        return render(request, 'uploading/upload_image.html', {'error': 'No image was uploaded!'})

    return render(request, 'uploading/upload_image.html')

# View for displaying uploaded images
def view_images(request):
    images = UploadImage.objects.all()
    return render(request, 'uploading/view_images.html', {'images': images})

