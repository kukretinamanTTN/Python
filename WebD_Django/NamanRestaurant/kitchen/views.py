from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import KitchenOrder
from customer.models import Order

@login_required
def kitchen_dashboard(request):
    orders = KitchenOrder.objects.all().order_by("-updated_at")
    return render(request, "kitchen/dashboard.html", {"orders": orders})

@login_required
def update_order_status(request, order_id, status):
    kitchen_order = get_object_or_404(KitchenOrder, order__id=order_id)
    kitchen_order.status = status
    kitchen_order.save()
    return redirect("kitchen_dashboard")
