from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignUpForm, NewUserForm
import ahpy, pyahp
from .models import College, StudyProgram, GradStudent

# homepage when accessing the site before signing up or logging in
def home(request):
    return render(request, 'index.html', {})


# the login page for the web app

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("dashboard.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


# the sign up or registration page
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            login(request, user='GradStudent')
            messages.success(request, ('You have been successfully signed up'))
            return redirect('dashboard.html')
        messages.error(request, "Unsuccessful registration ,please try again")
        return render(request, 'signup.html', {})

    else:
        return render(request, 'templates/signup.html', {})


# the page user interacts with after being logged in
def dashboard(request):
    return render(request, 'dashboard.html', {})


# the page user interacts with after being logged in
def profile(request):
    return render(request, 'profile.html', {})


#
def collegerating(request):
    return render(request, 'collegerating.html', {})


#
def collegeresults(request):
    return render(request, 'collegeresults.html', {})


#
def collegeselection(request):
    return render(request, 'collegesl.html', {})


#
def studyprogram(request):
    return render(request, 'studyprogram.html', {})


#
def programrating(request):
    return render(request, 'programrating.html', {})


#
def studyprogramresults(request):
    return render(request, 'studyprogramresults.html', {})



def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("CCApp:dashboard")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})




#
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("CCApp:dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})
