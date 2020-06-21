from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login_view"),
    path("register/", views.register_view, name="register_view"),
    path("homepage/", views.homepage_view, name="homepage_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("homepage/accountDetails/", views.accountDetails_view, name="accountDetails_view"),
    path("homepage/menu/", views.menu_view, name="menu_view"),
    path("homepage/shoppinCart/", views.shoppingCart_view, name="shoppingCart_view")
]
