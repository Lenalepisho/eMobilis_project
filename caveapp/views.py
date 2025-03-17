from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Booking
from .models import Contacts
from django.contrib.auth.decorators import login_required
import requests
import json
from caveapp.credentials import LipanaMpesaPpassword, MpesaAccessToken

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
    """Create a booking"""
    if request.method == 'POST':
        # Create a new booking associated with the logged-in user
        Booking.objects.create(
            user=request.user,  # Associate the booking with the logged-in user
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date_check_in=request.POST['date_check_in'],
            date_check_out=request.POST['date_check_out'],
            number=request.POST['number'],
            message=request.POST['message'],
        )
        return redirect('caveapp:my_bookings')  # Redirect to the user's bookings page
    return render(request, 'booking.html')

def retrieve_booking(request):
    """Retrieve and display all bookings (or modify it for user-specific bookings)."""
    booking = Booking.objects.all()
    return render(request, 'show_booking.html', {'booking': booking})

 # retrieve all appointments
@login_required
def my_bookings(request):
    """Retrieve and show bookings for the logged-in user"""
    user_bookings = Booking.objects.filter(user=request.user)  # Filter bookings by user
    context = {'booking': user_bookings}
    return render(request, 'show_booking.html', context)


    # delete
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


# views.py
def contact_view(request):
    """Contact Us"""
    if request.method == 'POST':
        # Create variable to pick the input fields
        contact = Contacts(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )



        contact.save()
        # Redirect to a page
        return redirect('caveapp:home')
    else:
        return render(request, 'contacts.html')

    

 # retrieve all appointments
def retrieve_contacts(request):
    """retrieve/fetch all contacts"""
# create variable to store these booking
    contacts=Contacts.objects.all()
    context= {'contacts':contacts}
    return render(request,'show_booking.html', context)




#Display the payment form
def pay(request):
   """ Renders the form to pay """
   return render(request, 'pay.html')


# Generate the ID of the transaction
def token(request):
    """ Generates the ID of the transaction """
    consumer_key = 'g2ex4qcL3259Ojq59CknURF0yCOA0ej4A5Pz6OA6iqQCmU19'
    consumer_secret = 'Afgk8LjDwNKVmFxlnKcUfSagMV5IBYubwW7GWdAZRIY3eZBbZW2HOS97rBh2OCev'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})


# Send the stk push
def stk(request):
    """ Sends the stk push prompt """
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("confirmed you have recieved")
