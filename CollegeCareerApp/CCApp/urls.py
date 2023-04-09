from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path("login/", views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/', views.dashboard, name="Dashboard"),
    path('profile/', views.profile, name="profile"),
    path('college/', views.college, name="colleges"),
    path('program/', views.program, name="program"),
    path('', include("django.contrib.auth.urls")),

]
