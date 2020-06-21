from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from orders.models import RegularPizza, SicilianPizza, Salad, Sub, Pasta, DinnerPlatter, Topping

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage_view'))
    else:
        return render(request, "orders/login.html", {"title": "Login"})

def login_view(request):
    if request.method == "POST":
        data = request.POST.copy()
        username = data.get("username")
        password = data.get("password")

        if username == '' or password == '':
            return render(request, "orders/login.html", {"title": "Login", "Message": "Any one of the fields is empty !"})

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage_view'))
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

        # More filtering required.

        if password != confirm_password:
            return render(request, "orders/register.html", {"title": "Register", "Message": "The Passwords dont match !"})

        elif username == '' or password == '' or confirm_password == '' or email == '' or first_name == '' or last_name == '':
            return render(request, "orders/register.html", {"title": "Register", "Message": "Any one of the fields is empty !"})

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        return render(request, "orders/login.html")

    elif request.method == "GET":
        return render(request, "orders/register.html", {"title": "Register"})
    

def homepage_view(request):
    return render(request, "orders/homepage.html", {"title": "Homepage", "Username": request.user.username})

def accountDetails_view(request):
    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email

    context = {
        "title": "Account Details",
        "Username": username,
        "FirstName": first_name,
        "LastName": last_name,
        "Email": email
    }

    return render(request, "orders/accountDetails.html", context)

def menu_view(request):

    context = {
        "title": "Menu", 
        "Username": request.user.username,
        "RegularPizza": RegularPizza.objects.all(),
        "SicilianPizza": SicilianPizza.objects.all(),
        "Toppings": Topping.objects.all(),
        "Subs": Sub.objects.all(),
        "Pasta": Pasta.objects.all(),
        "Salads": Salad.objects.all(),
        "DinnerPlatter": DinnerPlatter.objects.all()
    }

    return render(request, "orders/menu.html", context)

def shoppingCart_view(request):

    context = {
        "title": "Menu", 
        "Username": request.user.username,
        "RegularPizza": RegularPizza.objects.all(),
        "SicilianPizza": SicilianPizza.objects.all(),
        "Toppings": Topping.objects.all(),
        "Subs": Sub.objects.all(),
        "Pasta": Pasta.objects.all(),
        "Salads": Salad.objects.all(),
        "DinnerPlatter": DinnerPlatter.objects.all()
    }

    return render(request, "orders/shoppingCart.html", context)