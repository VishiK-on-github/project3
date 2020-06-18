from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from orders.models import RegularPizza, SicilianPizza, Salad, Sub, Pasta, DinnerPlatter, Topping

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "orders/homepage.html", {"title": "Homepage"})
    else:
        return render(request, "orders/login.html", {"title": "Login"})

def login_view(request):
    if request.method == "POST":
        data = request.POST.copy()
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Go to Homepage. 
            return render(request, "orders/homepage.html", {"title": "Homepage"})
        else:
            return render(request, "orders/login.html", {"title": "Login", "Message": "Username or password is incorrect !"})
    elif request.method == "GET":
        return render(request, "orders/login.html", {"title": "Login"})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register_view(request):
    if request.method == "POST":
        data = request.POST.copy()
        username = data.get("username")
        password = data.get("password")
        confirm_password = data.get("cpassword")
        email = data.get("email")
        first_name = data.get("fname")
        last_name = data.get("lname") 

        if password != confirm_password:
            return render(request, "orders/register.html", {"title": "Register", "Message": "The Passwords dont match !"})

        elif username == '' or password == '' or confirm_password == '' or email == '' or first_name == '' or last_name == '':
            return render(request, "orders/register.html", {"title": "Register", "Message": "Any one of the fields is empty !"})

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        return render(request, "orders/login.html")

    elif request.method == "GET":
        return render(request, "orders/register.html", {"title": "Register"})
    