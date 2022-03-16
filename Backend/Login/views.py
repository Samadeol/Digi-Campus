from django.shortcuts import render, redirect
#from .serializers import ProfileSerializer
from .models import Profile
#from rest_framework import viewsets
# Create your views here.

glob_id=0
def login_view(request,*args,**kwargs):
    profiles = Profile.objects.all()
    # for pro in profiles:
    #     print (pro.login)
    #     if pro.login == True:
    #         return redirect("../profile/")
    if request.method == "POST" :
        user = request.POST.get('User ID')
        passw = request.POST.get('password')
        #pro = profile.ob
        #profiles = Profile.objects.all()
        userid=0
        for pro in profiles:
            userid=userid+1
            if pro.username == user and pro.password == passw:
                pro.login = True
                
                glob_id=userid
                return redirect("../profile/"+str(userid))
            
        #print(username+ " " + password)
    return render(request,"login.html",{})


def profile_view(request,id):
    user=Profile.objects.get(id=id)
    context={"username":user.username,"first_name":user.first_name,"last_name":user.last_name,"room_no":user.room_no,
    "hall_no":user.hall_no,"email":user.email,"profile_id":str(id),"pwd":user.password,"roll_no":user.roll_no,"mobile_no":user.mobile_no}
    return render(request,"profile.html",context)


def dashboard_view(request,*args,**kwargs):
   # user=Profile.objects.get(id=glob_id)
    #context={"username":user.username,"name":user.full_name}
    return render(request,"mess.html")



    