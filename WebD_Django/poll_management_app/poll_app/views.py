from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count
from django.views import View
from .models import Poll
import logging

class PollDetailView(View):
    def get(self, request, poll_id):
        poll = get_object_or_404(Poll, id=poll_id)
        return render(request, 'poll_app/poll_detail.html', {'poll': poll})

def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'poll_app/poll_list.html', {'polls': polls})

# @login_required
# def poll_detail(request, poll_id):
#     poll = get_object_or_404(Poll, id=poll_id)
#     return render(request, 'poll_app/poll_detail.html', {'poll': poll})

@login_required
@permission_required('poll_app.can_view_results', raise_exception=True)
def poll_statistics(request):
    stats = Poll.objects.annotate(total_votes=Count('id'))
    return render(request, 'poll_app/statistics.html', {'stats': stats})


logger = logging.getLogger(__name__)
def vote(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    logger.info(f"User {request.user} voted in poll {poll.question}")
    return render(request, 'poll_app/poll_list.html')
