from django.db import models
from customer.models import Order

class KitchenOrder(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("preparing", "Preparing"),
        ("ready", "Ready for Pickup"),
        ("delivered", "Delivered"),
    ]
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order.id} - {self.status}"
