from django.shortcuts import render, redirect
#from .serializers import ProfileSerializer
from .models import Profile
#from rest_framework import viewsets
# Create your views here.

def login_view(request,*args,**kwargs):
    profiles = Profile.objects.all()
    for pro in profiles:
        print (pro.login)
        if pro.login == True:
            return redirect("../mess/")
    if request.method == "POST" :
        user = request.POST.get('User ID')
        passw = request.POST.get('password')
        #pro = profile.ob
        #profiles = Profile.objects.all()
        for pro in profiles:
            if pro.username == user and pro.password ==passw:
                pro.login = True
                return redirect("../mess/")
        #print(username+ " " + password)
    return render(request,"login.html",{})