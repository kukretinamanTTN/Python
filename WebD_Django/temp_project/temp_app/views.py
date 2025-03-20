from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, Vote

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("poll_questions")  # Redirects to poll list
    else:
        form = AuthenticationForm()
    return render(request, "temp_app/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def poll_questions(request):
    questions = Question.objects.all()
    voted_questions = Vote.objects.filter(user=request.user).values_list("question_id", flat=True)

    return render(request, "temp_app/poll_questions.html", {
        "questions": questions,
        "voted_questions": voted_questions
    })

@login_required
def vote_question(request):
    if request.method == "POST":
        choice_id = request.POST.get("choice_id")  # Get selected choice
        choice = get_object_or_404(Choice, id=choice_id)
        user = request.user

        # Check if the user has already voted for this question
        if Vote.objects.filter(user=user, question=choice.question).exists():
            return HttpResponse("You have already voted in this poll!", status=403)

        # Record the vote
        choice.votes += 1
        choice.save()
        Vote.objects.create(user=user, question=choice.question, choice=choice)

    return redirect("poll_questions")  # Redirect to the poll list
