from django import forms
from sympy import Q
from .models import HallStudents, hallPresence
from Login.models import Profile
from django.contrib.auth.models import User
class EntryForm(forms.Form):
    user_visiting=forms.CharField(label='Roll Number Visiting',widget=forms.TextInput(attrs={"placeholder":"Roll Number Visiting"}))
    laptop=forms.CharField(label='Laptop (Yes/No)',widget=forms.TextInput(attrs={"placeholder":"Yes/No"}))