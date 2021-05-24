from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from my_polls.models import Poll, PollAnswer
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    user = User.objects.get(id=request.user.id)
    last_polls = Poll.objects.exclude(author=user).exclude(answered_by__username__exact=user.username).order_by('-id')[:9]

    return render(request, 'polls/index.html', {'polls':last_polls})

@login_required
def answer_poll(request, id):
    poll = get_object_or_404(Poll, id=id)

    if poll.author.id == request.user.id:
        messages.error(request, 'You cannot answer your own poll!')
        return redirect('main_index')
    
    if request.user.id in [ans_user.id for ans_user in poll.answered_by.all()]:
        messages.error(request, 'You have already answered this poll')
        return redirect('main_index')
    
    if request.method == 'POST':
        questions = poll.questions.all()

        for i in range(len(questions)):
            answer_voted_num = int(request.POST[f'question-{i+1}'][-1])
            answer_voted = questions[i].answers.all()[answer_voted_num-1]
            answer_voted.votes += 1
            answer_voted.save()

        poll.answered_by.add(User.objects.get(id=request.user.id))

        messages.success(request, 'Your answer to the poll have been sent correctly')
        return redirect('main_index')

    return render(request, 'polls/answer.html', {'poll':poll})

@login_required
def search(request):
    if request.method == 'POST':
        query = request.POST['query']

        if 'author:' in query:
            polls = Poll.objects.filter(author__username__icontains=query.split(':')[-1]).exclude(author=User.objects.get(id=request.user.id)).exclude(answered_by__username__exact=request.user.username)
        else:
            polls = Poll.objects.filter(title__icontains=query).exclude(author=User.objects.get(id=request.user.id)).exclude(answered_by__username__exact=request.user.username)

        return render(request, 'polls/search.html', {'polls':polls, 'query':query})

    messages.error(request, 'Search a poll from the search bar')
    return redirect('main_index')