from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.

def register(request):
         
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1") 
        password2 = request.POST.get("password2")

      # VALIDATIONS

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("register")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")
 
      # CREATE USER

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=fname,
            last_name=lname
        )

        messages.success(request, "Account created successfully!")
        return redirect("login")

    return render(request, 'register.html')



def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # AUTHENTICATE USING EMAIL

        try:
            user_obj = User.objects.get(email=email)

            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )

        except User.DoesNotExist:
            user = None

        # CHECK AUTHENTICATION

        if user is not None:

            auth_login(request, user)

            messages.success(request, "Login successful!")

            return redirect("index")  # Change to dashboard later

        else:
            messages.error(request, "Invalid email or password!")

            return redirect("login")

    return render(request, 'login.html')



def logout_view(request):
    
    auth_logout(request)

    messages.success(request, "You have been logged out successfully!")

    return redirect("login")