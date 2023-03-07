from django.shortcuts import render
from django.contrib import messages
from .forms import SignUpForm


# homepage when accessing the site before signing up or logging in
def home(request):
    return render(request, 'index.html', {})


# the login page for the web app
def login(request):
    return render(request, 'login.html', {})


# the sign up or registration page
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have been successfully signed up'))
        return render(request, 'signup.html', {})

    else:
        return render(request, 'signup.html', {})


# the page user interacts with after being logged in
def dashboard(request):
    return render(request, 'dashboard.html', {})
