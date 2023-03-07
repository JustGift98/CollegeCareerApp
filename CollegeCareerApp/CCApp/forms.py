from django import forms
from .models import GradStudent


class SignUpForm(forms.ModelForm):
    class Meta:
        model = GradStudent
        fields = ['fname', 'lname', 'email', 'DOB', 'password', 'gender']
