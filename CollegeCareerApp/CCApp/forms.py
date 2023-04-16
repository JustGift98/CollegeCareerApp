from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

        def save(self, commit=True):
            user = super(SignUpForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user



class Crit_model_form(forms.ModelForm):
    class Meta:
        model = Crit_model
        fields = ('name',)


class Criteria_form(forms.ModelForm):
    class Meta:
        model = Criteria
        fields = ('crit1', 'crit2', 'crit3',)


class Element_form(forms.ModelForm):
    class Meta:
        model = Element
        fields = ('name', 'attrib1', 'attrib2', 'attrib3', 'attrib4',)
        labels = {
            "name": "Nazwa",
            "attrib1": "Nazwa",
            "attrib2": "Nazwa",
            "attrib3": "Nazwa",
            "attrib4": "Nazwa",
        }





