from django import forms
from sympy import Q
from .models import HallStudents, hallPresence
from Login.models import Profile
from django.contrib.auth.models import User
Choices=[
    ('Yes','Yes'),
    ('No','No')
]
class EntryForm(forms.Form):
    user_visiting=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Roll Number Visiting"}))
    room_number=forms.CharField(label='Room Number',widget=forms.TextInput(attrs={"placeholder":"Room Number"}))
    laptop=forms.CharField(label='Laptop',widget=forms.Select(choices=Choices))

class ExitForm(forms.Form):
    exit=forms.BooleanField(label='Do you want to exit?',widget=forms.BooleanField())