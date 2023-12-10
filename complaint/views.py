from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import complaint

# Create your views here.

def home(request):
    return render(request, "home.html" )


def register(request):
    if request.method == 'POST':
      
        uname = request.POST.get('username', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        mail = request.POST.get('email', '')
        pass1 = request.POST.get('password', '')

    

        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, "register.html") # Redirect back to registration page
        elif User.objects.filter(email=mail).exists():
            messages.error(request, 'Email already exists. Please use a different one.')
            return render(request, "register.html") # Redirect back to registration page
        else:
            user = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=mail, password=pass1)
            user.save()
            return render(request,"login.html") # Redirect to login page after successful registration
    else:
        return render(request, "register.html")


def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
             # Successful login
            auth.login(request, user)
            return redirect('complaint_list')
        else:
            # Invalid login credentials
            messages.info(request, "Invalid Username or Password")
    return render(request, "login.html" )


def complaint_list(request):
    complaints = complaint.objects.all()
    return render(request, 'complaint_list.html', {'complaints': complaints})

def submit_complaint(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        complaint.objects.create(title=title, description=description)
        return render(request, 'complaint_submitted.html')
    return render(request, 'submit_complaint.html')

def complaint_submitted(request):
    # Logic to handle the page after submission
    return render(request, 'complaint_submitted.html')


