from django.urls import path
from .views import kitchen_dashboard, update_order_status

urlpatterns = [
    path("", kitchen_dashboard, name="kitchen_dashboard"),
    path("update/<int:order_id>/<str:status>/", update_order_status, name="update_order_status"),
]
