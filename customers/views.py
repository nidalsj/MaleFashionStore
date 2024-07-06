from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Customer
from django.contrib.auth import authenticate, login, logout


def signupuser(request):
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("pass1")
        repassword = request.POST.get("pass2")

        # password length
        if len(password) < 8:
            messages.error(request, 'Password is too short')
            return render(request, 'signup.html')

        # email and password are the same
        if email == password:
            messages.error(request, 'Email and password cannot be the same')
            return render(request, 'signup.html')

        # email or phone number already exists
        if User.objects.filter(email=email).exists() or User.objects.filter(username=phone).exists():
            messages.error(request, 'This user already exists')
            return render(request, 'signup.html')
        
        # phone number length
        if len(phone) != 10:
            messages.error(request, 'Phone number must be 10 digits')
            return render(request, 'signup.html')

        # phone number is same as the password
        if phone == password:
            messages.error(request, 'Phone number cannot be your password')
            return render(request, 'signup.html')

        # passwords match
        if password != repassword:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')

        # new user
        user = User.objects.create_user(
            username=email,
            password=password,
            email=email,
            first_name=fullname
        )

        # a new customer account
        customer = Customer.objects.create(
            first_name=fullname,
            user=user,
            email=email,
            phone=phone
        )

        messages.success(request, 'Account created. Please log in')
        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')


def loginuser(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        # check if the user exists
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid user. You need to signup first')
            return render(request, 'signup.html')
    else:
        return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('home')


def user_profile(request):
    return render(request, 'user_profile.html')