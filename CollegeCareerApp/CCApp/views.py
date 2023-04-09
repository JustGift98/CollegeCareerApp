from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm



# homepage when accessing the site before signing up or logging in
def home(request):
    return render(request, 'index.html', {})


# the login page for the web app
def login(request):
    return render(request, 'login.html', {})

def signup(response):
    if response.method == 'POST':
        form = SignUpForm(response.POST)
        if form.is_valid():
            user = form.save()


            # redirect user to home page
            return redirect('dashboard.html')
    else:
        form = SignUpForm()
    return render(response, 'signup.html', {'form': form})



# the page user interacts with after being logged in
def dashboard(request):
    return render(request, 'dashboard.html', {})


def profile(request):
    return render(request, 'profile.html', {})

def college(request):
    return render(request, 'collegesl.html', {})

def program(request):
    return render(request, 'studyprogram.html', {})