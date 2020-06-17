from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from orders.models import RegularPizza, SicilianPizza, Salad, Sub, Pasta, DinnerPlatter, Topping

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")

def login_view(request):
    if request.method == "POST":
        username = request.POST("username")
        password = request.POST("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Go to Homepage. 
        else:
            return render(request, "orders/login.html", {"title": "Login"})
    elif request.method == "GET":
        return render(request, "orders/login.html", {"title": "Login"})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html")

def register_view(request):
    if request.method == "POST":
        '''username = request.POST("username")
        password = request.POST("password")
        confirm_password = request.POST("cpassword")
        email = request.POST("email")
        first_name = request.POST("fname")
        last_name = request.POST("lname")'''

    elif request.method == "GET":
        return render(request, "orders/register.html", {"title": "Register"})
    