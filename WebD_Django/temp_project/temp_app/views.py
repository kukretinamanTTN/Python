from django.shortcuts import render, redirect
from .models import Question, Choice
from django.views import View
from django.http import HttpResponse

def poll_question(request):
    questions = Question.objects.all()
    return render(request, 'temp_app/poll_questions.html', {'questions':questions})

def vote_question(request, choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.votes += 1
    choice.save()
    return redirect('poll_question')

class ClassBasedViews(View):
    def get(self, request):
        return HttpResponse("This is a class based view")
    
def function_based_view(request):
    return HttpResponse("This is a function based view")