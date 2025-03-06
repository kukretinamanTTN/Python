import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import FoodItem, Order, OrderItem

#change Django admin site specifications
admin.site.site_header = "Naman Restaurant Admin Panel"
admin.site.site_title = "Restaurant Management"
admin.site.index_title = "Welcome to the Dashboard"

#csv download
def download_csv(*_, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="food_items.csv"'

    writer = csv.writer(response)
    writer.writerow(["ID", "Name", "Description", "Price"])  #CSV Headers

    for item in queryset:
        writer.writerow([item.id, item.name, item.description, item.price])  #CSV Data

    return response

#admin actions
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "description")  #columns in admin panel
    list_filter = ("price",)  #add price filter
    search_fields = ("name", "description")  #enable search in admin panel
    ordering = ("id",)  #sort by ID by default
    actions = [download_csv]  #register the admin action

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "total_price", "created_at")
    list_filter = ("created_at",)
    search_fields = ("customer__username",)
    inlines = [OrderItemInline]


admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Order, OrderAdmin)
