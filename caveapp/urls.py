from django.urls import path
from . import views

app_name="caveapp"
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),

    path('events/', views.events, name="events"),
    path('chefs/', views.chefs, name="chefs"),
    path('gallery/', views.gallery, name="gallery"),
    path('contacts/', views.contacts, name="contacts"),
    path('booking/', views.booking, name="booking"),
    path('show_booking/', views.retrieve_booking, name="show_booking"),
    path('delete/<int:id>', views.delete_booking, name="delete_booking"), #delete
    path('edit/<int:booking_id>',views.update_booking, name="update_booking"),
]
