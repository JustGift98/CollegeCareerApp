from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("login", views.login_request, name="login"),
    path('signup', views.signup, name="signup"),
    path('dashboard', views.dashboard, name="Dashboard"),
    path('profile', views.profile, name="profile"),
    path('collegerating', views.collegerating, name="collegerating"),
    path('collegeselection', views.collegeselection, name="collegeselection"),
    path('collegeresults', views.collegeresults, name="collegeresulsts"),
    path('studyprogram', views.studyprogram, name="studyprogram"),
    path('studyprogramresults', views.studyprogramresults, name="studyprogramresults"),
    path('programrating', views.programrating, name="programrating"),
    path("register", views.register_request, name="register")
]
