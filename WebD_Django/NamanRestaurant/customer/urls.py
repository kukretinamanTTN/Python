from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("menu/", menu_view, name="menu"),
    path("add_to_cart/<int:food_id>/", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:food_id>/", remove_from_cart, name="remove_from_cart"),
    path("clear_cart/", clear_cart, name="clear_cart"),
    path("place_order/", place_order, name="place_order"),
    path("orders/", orders_view, name="orders"),
]
