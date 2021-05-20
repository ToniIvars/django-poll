from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    questions = models.ManyToManyField('PollQuestion', related_name='questions')
    answered_by = models.ManyToManyField(User, related_name='answered_by')

    def __str__(self):
        return f'{self.title} by {self.author}'

class PollQuestion(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll')
    title = models.CharField(max_length=200)
    answers = models.ManyToManyField('PollAnswer', related_name='answers')

    def __str__(self):
        return f'{self.title} from {self.poll}'

class PollAnswer(models.Model):
    question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE, related_name='question')
    answer = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.answer} from {self.question}'