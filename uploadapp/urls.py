from django.urls import path
from . import views

app_name="uploadapp"
urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.view_images, name='view_images'),
    path('upload/success/', views.upload_success, name='upload_success'),
]
