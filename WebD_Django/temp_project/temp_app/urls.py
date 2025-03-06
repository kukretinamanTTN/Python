from django.urls import path
from .views import *

urlpatterns = [
    path('all_polls/', poll_question, name='poll_question'),
    path('all_choices/<int:choice_id>', vote_question, name='vote_question')
]