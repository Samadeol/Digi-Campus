from django import forms
from sympy import Q
from .models import hallPresence

class EntryForm(forms.ModelForm):
    room   =forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Room Number"}))
    roll   =forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Room Number"}))
    laptop  =forms.NullBooleanSelect()
    
    class Meta:
        model=hallPresence
        fields=['room','roll','laptop']