from django.shortcuts import render,redirect,get_object_or_404
from .models import Booking
from .models import Contacts
from django.contrib.auth.decorators import login_required

def home(request):
    """display home page"""
    return render(request, "index.html")

def about(request):
    """display about page"""
    return render(request, "about.html")

def chefs(request):
    """display chefs page"""
    return render(request, "chefs.html")

def contacts(request):
    """display contacts page"""
    return render(request, "contacts.html")

def events(request):
    """display events page"""
    return render(request, "events.html")

def menu(request):
    """display menu page"""
    return render(request, "menu.html")



def gallery(request):
    """display gallery page"""
    return render(request, "gallery.html")

def booking(request):
    """display booking page"""
    return render(request, "booking.html")

def show_booking(request):
    """display show booking page"""
    return render(request, "show_booking.html")



@login_required
def booking(request):
    """create booking"""
    if request.method == 'POST':
       #Create variable to pick the input fields
        booking = Booking(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date_check_in = request.POST['date_check_in'],
            date_check_out = request.POST['date_check_out'],
            number = request.POST['number'],
            message = request.POST['message'],       
        )

        booking.save()
        #redirect to a page
        return redirect('caveapp:home')
    else:
        return render(request, 'booking.html',)
    

 # retrieve all appointments
def retrieve_booking(request):
    """retrieve/fetch all booking"""
# create variable to store these booking
    booking=Booking.objects.all()
    context= {'booking':booking}
    return render(request,'show_booking.html', context)

    delete
def delete_booking(request,id):
    """deleting"""
    booking=Booking.objects.get(id=id) #fetch particular booking
    booking.delete()
    return redirect("caveapp:show_booking") #just remain on same page


# update
def update_booking(request, booking_id):
    """update the booking"""
    booking=get_object_or_404(Booking, id=booking_id)
    #put the condition for the form to update
    if request.method=='POST':
        booking.name=request.POST.get('name')
        booking.email=request.POST.get('email')
        booking.phone=request.POST.get('phone')
        booking.date_check_in = request.POST.get('date_check_in')
        booking.date_check_out = request.POST.get('date_check_out')
        booking.number = request.POST.get('number')
        booking.message=request.POST.get('message')
        
       

        # once you click on the update button
        booking.save()
        return redirect('caveapp:show_booking')
    context={'booking':booking}
    return render(request, "update_booking.html",context)


def Contacts(request):
    """Contact Us"""
    if request.method == 'POST':
       #Create variable to pick the input fields
        contacts = Contacts(
            name = request.POST['name'],
            email = request.POST['email'],
           subject= request.POST['subject'],
            message = request.POST['message'],       
        )

        contacts.save()
        #redirect to a page
        return redirect('caveapp:home')
    else:
        return render(request, 'contacts.html',)
    

 # retrieve all appointments
def retrieve_contacts(request):
    """retrieve/fetch all contacts"""
# create variable to store these booking
    contacts=Contacts.objects.all()
    context= {'contacts':contacts}
    return render(request,'show_booking.html', context)
