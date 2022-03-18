from django import forms
from sympy import Q
from .models import HallStudents, hallPresence
from Login.models import Profile
from django.contrib.auth.models import User
class EntryForm(forms.ModelForm):
    # room_no =forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Room Number"}))
    user_visiting=forms.IntegerField(label='',widget=forms.TextInput(attrs={"placeholder":"Roll Number Visiting"}))
    laptop=forms.BooleanField()
    
    class Meta:
        model=hallPresence
        fields=['user_visiting','laptop']