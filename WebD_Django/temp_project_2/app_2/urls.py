from django.urls import path
from .views import VoteFormView, PollResultsView

urlpatterns = [
    path('<int:poll_id>/vote/', VoteFormView.as_view(), name='vote_poll'),
    path('<int:pk>/results/', PollResultsView.as_view(), name='poll_results'),
]
