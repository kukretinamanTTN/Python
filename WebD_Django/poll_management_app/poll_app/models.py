from django.db import models
from django.contrib.auth.models import User

class PollManager(models.Manager):
    def active_polls(self):
        return self.filter(is_active=True)
    
class Poll(models.Model):
    question = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    #custom manager
    active_polls = PollManager()

    #default manager
    objects = models.Manager()

    class Meta:
        permissions = [
            ("can_view_results", "Can view poll results"),
        ]

    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
