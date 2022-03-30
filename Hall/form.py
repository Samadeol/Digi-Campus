from cProfile import label
from django import forms
from sympy import Q
from Login.models import Profile
from django.contrib.auth.models import User
Choices=[
    ('Yes','Yes'),
    ('No','No')
]
class EntryForm(forms.Form):
    # first_name=forms.CharField(max_length=40,label='First Name',widget=forms.TextInput(attrs={"placeholder":"First Name"}))
    # last_name=forms.CharField(max_length=40,label='First Name',widget=forms.TextInput(attrs={"placeholder":"First Name"}))
    # mobile_number=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Mobile Number"}))
    # roll_number=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Roll Number"}))
    user_visiting=forms.IntegerField(widget=forms.TextInput(attrs={"placeholder":"Roll Number Visiting"}))
    room_number=forms.CharField(label='Room Number',widget=forms.TextInput(attrs={"placeholder":"Room Number"}))
    laptop=forms.CharField(label='Laptop',widget=forms.Select(choices=Choices))

class ExitForm(forms.Form):
    exit=forms.BooleanField(label='Do you want to exit?',widget=forms.BooleanField())