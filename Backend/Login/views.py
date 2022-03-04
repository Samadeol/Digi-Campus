from django.shortcuts import render
from .models import Profile
# Create your views here.

def login_view(request,*args,**kwargs):
    if request.method == "POST" :
        user = request.POST.get('User ID')
        passw = request.POST.get('password')
        #pro = profile.ob
        profiles = Profile.objects.all()
        flag = False
        for pro in profiles:
            if pro.username == user and pro.password ==passw :
                print("yooo")
                flag = True
                break
        if not flag : print("no")
        #print(username+ " " + password)
    return render(request,"login.html",{})