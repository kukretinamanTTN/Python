from django.urls import path
from .views import poll_list, poll_statistics, PollDetailView
urlpatterns = [
    path('', poll_list, name='poll_list'),
    path('<int:poll_id>/', PollDetailView.as_view(), name='poll_detail'),
    path('statistics/', poll_statistics, name='poll_statistics'),
]
