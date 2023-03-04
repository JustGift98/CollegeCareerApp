from django.shortcuts import render
from .models import GradStudent, College, StudyProgram


# homepage when accessing the site before signing up or logging in
def home(request):
    return render(request, 'index.html', {})


# the login page for the web app
def login(request):
    return render(request, 'login.html', {})


# the sign up or registration page
def signup(request):

    return render(request, 'signup.html', {})


# the page user interacts with after being logged in
def dashboard(request):

    return render(request, 'dashboard.html', {})
