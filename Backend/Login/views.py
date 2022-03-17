from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import user_passes_test
#from .serializers import ProfileSerializer
from .models import Profile
#from rest_framework import viewsets
# Create your views here.

glob_id=0

def login_view(request,*args,**kwargs):
    profiles = Profile.objects.all()
    if request.method == "POST" :
        user = request.POST.get('User ID')
        passw = request.POST.get('password')
        userid=0
        for pro in profiles:
            userid=userid+1
            if pro.username == user and pro.password ==passw:
                global glob_id 
                glob_id=userid
                print(pro.logged_in,pro.username)
                return redirect("../profile/"+str(userid))
    return render(request,"login.html",{})


def profile_view(request,id):
    user=Profile.objects.get(id=id)
    # if(user.logged_in == False):
    #     return redirect("../login")
    print(glob_id)
    if(glob_id!=id): return redirect("../login")
    context={"username":user.username,"name":user.full_name,"profile_id":str(id)}
    
    return render(request,"profile.html",context)


def dashboard_view(request,*args,**kwargs):
   # user=Profile.objects.get(id=glob_id)
    #context={"username":user.username,"name":user.full_name}
    return render(request,"mess.html")

def qr_view(request,*args,**kwargs):
    return render(request,"qr_code.html")
    