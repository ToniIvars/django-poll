from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from my_polls.models import Poll, PollAnswer
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    last_polls = Poll.objects.exclude(author=User.objects.get(id=request.user.id)).order_by('-id')[:9]
    return render(request, 'polls/index.html', {'polls':last_polls})

@login_required
def answer_poll(request, id):
    poll = get_object_or_404(Poll, id=id)

    if poll.author.id == request.user.id:
        messages.error(request, 'You cannot answer your own poll!')
        return redirect('main_index')
    
    if request.method == 'POST':
        questions = poll.questions.all()
        print(questions)

        for i in range(len(questions)):
            answer_voted_num = int(request.POST[f'question-{i+1}'][-1])
            answer_voted = questions[i].answers.all()[answer_voted_num-1]
            answer_voted.votes += 1
            answer_voted.save()

        messages.success(request, 'Your answerd to the poll have been sent correctly')
        return redirect('main_index')

    return render(request, 'polls/answer.html', {'poll':poll})