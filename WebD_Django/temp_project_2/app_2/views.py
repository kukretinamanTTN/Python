from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Poll
from .forms import VoteForm

class VoteFormView(FormView):
    template_name = 'app_2/vote.html'
    form_class = VoteForm

    def get_form_kwargs(self):
        """Pass the current poll to the form"""
        kwargs = super().get_form_kwargs()
        self.poll = get_object_or_404(Poll, pk=self.kwargs['poll_id'])
        kwargs['poll'] = self.poll
        return kwargs
    
    def get_context_data(self, **kwargs):
        """Pass poll data to the template"""
        context = super().get_context_data(**kwargs)
        context['poll'] = self.poll
        return context

    def form_valid(self, form):
        """Increase vote count for the selected choice"""
        choice = form.cleaned_data['choice']
        choice.votes += 1
        choice.save()
        return redirect(reverse_lazy('poll_results', kwargs={'pk': choice.poll.id}))


class PollResultsView(DetailView):
    model = Poll
    template_name = 'app_2/poll_results.html'
    context_object_name = 'poll'
