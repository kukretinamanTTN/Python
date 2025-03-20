from django.urls import path
from .views import login_view, logout_view, poll_questions, vote_question

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("all_polls/", poll_questions, name="poll_questions"),  # Correct view name
    path("vote/", vote_question, name="vote_question"),  # No choice_id in URL (handled via POST)
]
