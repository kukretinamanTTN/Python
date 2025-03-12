from django.views.generic import ListView, DetailView
from .models import Question

class QuestionListView(ListView):
    model = Question
    template_name = 'viewapp/question_list.html'
    context_object_name = 'questions'
    paginate_by = 2

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'viewapp/question_detail.html'
    context_object_name = 'question'

