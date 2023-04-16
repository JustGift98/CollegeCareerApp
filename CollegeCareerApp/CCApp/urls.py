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
    path('crit_model_details/<int:pk>/', views.crit_model_details, name='crit_model_details'),
    path('crit_model_details/<int:pk>/modify_criterias/', views.modify_criterias, name='modify_criterias'),
    path('crit_model_details/<int:pk>/modify_elements/', views.modify_elements, name='modify_elements'),
    path('crit_model_details/<int:pk>/solve/', views.solve, name='solve'),
    path('crit_model_details/<int:pk>/solver/', views.solver, name='solver'),

]
