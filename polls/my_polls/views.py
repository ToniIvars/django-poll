from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Poll, PollQuestion, PollAnswer
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    polls = Poll.objects.filter(author=User.objects.get(id=request.user.id))
    return render(request, 'my_polls/index.html', {'polls':polls})

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