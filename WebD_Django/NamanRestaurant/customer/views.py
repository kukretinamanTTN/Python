from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.contrib import messages
from .models import FoodItem, Order, OrderItem

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("menu")
    else:
        form = UserCreationForm()
    return render(request, "customer/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("menu")
    else:
        form = AuthenticationForm()
    return render(request, "customer/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def menu_view(request):
    search_query = request.GET.get("search", "").strip()
    max_price = request.GET.get("max_price", "").strip()

    #filtering using name and description
    filters = Q()
    if search_query:
        filters &= Q(name__icontains=search_query) | Q(description__icontains=search_query)
    if max_price:
        filters &= Q(price__lte=float(max_price))
    food_items = FoodItem.objects.filter(filters)

    #cart retrieval
    cart = request.session.get("cart", {})
    cart_items = []
    total_price = 0
    for item_id, quantity in cart.items():
        food = FoodItem.objects.get(id=item_id)
        cart_items.append({"food": food, "quantity": quantity})
        total_price += food.price * quantity

    return render(
        request,
        "customer/menu.html",
        {
            "food_items": food_items,
            "cart_items": cart_items,
            "total_price": total_price,
            "search_query": search_query,
            "max_price": max_price,
        },
    )

@login_required
def add_to_cart(request, food_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        cart = request.session.get("cart", {})

        #add or increase quantity
        if str(food_id) in cart:
            cart[str(food_id)] += quantity
        else:
            cart[str(food_id)] = quantity

        request.session["cart"] = cart
        return redirect("menu")

@login_required
def remove_from_cart(request, food_id):
    cart = request.session.get("cart", {})
    
    # Remove the item if it afterexists
    if str(food_id) in cart:
        del cart[str(food_id)]
    
    request.session["cart"] = cart
    return redirect("menu")


@login_required
def place_order(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect("menu")
    total_price = sum(FoodItem.objects.get(id=item_id).price * quantity for item_id, quantity in cart.items())
    order = Order.objects.create(customer=request.user, total_price=total_price)

    for item_id, quantity in cart.items():
        food_item = FoodItem.objects.get(id=item_id)
        OrderItem.objects.create(order=order, food_item=food_item, quantity=quantity)

    #clear cart after placing order
    request.session["cart"] = {}  
    messages.success(request, "Order placed successfully!")
    return redirect("orders")

@login_required
def clear_cart(request):
    request.session["cart"] = {}  #clear cart in session
    return redirect("menu")

@login_required
def orders_view(request):
    orders = Order.objects.filter(customer=request.user).order_by("-created_at")
    return render(request, "customer/orders.html", {"orders": orders})