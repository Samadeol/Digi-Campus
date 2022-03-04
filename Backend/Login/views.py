from django.shortcuts import render
from .models import profile
# Create your views here.

def login_view(request,*args,**kwargs):
    return render(request,"login.html",{})