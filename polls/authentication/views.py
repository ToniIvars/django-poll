from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, SignupForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return redirect('main_index')

            messages.error(request, 'The username or the password are incorrect')
            return redirect('login')
            
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form':form})

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            login(request, user)
            return redirect('main_index')
            
    else:
        form = SignupForm()

    return render(request, 'authentication/signup.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')