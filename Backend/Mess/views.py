from django.shortcuts import render
from .models import messMenu
# Create your views here.
def mess_view(request,*args,**kwargs):
    return render(request,"mess_profile/mess.html",{'BDMR':'50'})