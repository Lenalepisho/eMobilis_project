from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('caveapp:my_bookings')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html')

# logout function
def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('accountapp:login')  # Redirect to the login page


# register
def register(request):
    """Show the registration form and handle user registration"""
    if request.method == 'POST':
        # Get form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use')
            else:
                # Create the user if validation passes
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                messages.success(request, "Account created successfully")
                return redirect('caveapp:home')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'accounts/register.html')
