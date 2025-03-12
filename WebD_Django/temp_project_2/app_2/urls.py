from django.urls import path
from .views import *

urlpatterns = [
    path('form/', contact_view, name='contact_view'),
]