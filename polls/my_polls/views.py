from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Poll, PollQuestion, PollAnswer
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    polls = Poll.objects.filter(author=User.objects.get(id=request.user.id))

    answered_by = []
    for poll in polls:
        num = 0
        for ans in poll.questions.first().answers.all():
            num += ans.votes

        answered_by.append(num)
        
    return render(request, 'my_polls/index.html', {'polls':polls, 'answered_by':answered_by})

@login_required
def create_poll(request):
    if request.method == 'POST':
        title = request.POST['title']
        poll = Poll.objects.create(title=title, author=User.objects.get(id=request.user.id))

        num = 1
        while True:
            try:
                question = PollQuestion.objects.create(poll=poll, title=request.POST[f'question_title_{num}'])

                ans1 = PollAnswer.objects.create(question=question, answer=request.POST[f'answer_{num}_1'])
                question.answers.add(ans1)

                ans2 = PollAnswer.objects.create(question=question, answer=request.POST[f'answer_{num}_2'])
                question.answers.add(ans2)

                if request.POST.get(f'answer_{num}_3', False):
                    ans3 = PollAnswer.objects.create(question=question, answer=request.POST[f'answer_{num}_3'])
                    question.answers.add(ans3)
                
                if request.POST.get(f'answer_{num}_4', False):
                    ans4 = PollAnswer.objects.create(question=question, answer=request.POST[f'answer_{num}_4'])
                    question.answers.add(ans4)
                
                poll.questions.add(question)
                num += 1

            except:
                break
        
        return redirect('my_polls_index')

    return render(request, 'my_polls/create.html')

@login_required
def delete_poll(request, id):
    poll = get_object_or_404(Poll, id=id)

    if poll.author.id != request.user.id:
        messages.error(request, 'You cannot delete a poll that is not yours!')
        return redirect('my_polls_index')

    if request.method == 'POST':
        poll.delete()

        messages.success(request, 'Poll deleted successfully')
        return redirect('my_polls_index')
    
    return render(request, 'my_polls/delete.html', {'id':poll.id})

@login_required
def poll_statics(request, id):
    poll = get_object_or_404(Poll, id=id)

    if poll.author.id != request.user.id:
        messages.error(request, 'You cannot view the poll statics of a poll that is not yours')
        return redirect('my_polls_index')

    return render(request, 'my_polls/statics.html', {'poll':poll})