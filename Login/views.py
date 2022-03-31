from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.http import Http404,HttpResponse
from django.contrib.auth.decorators import user_passes_test
#from .serializers import ProfileSerializer
# from .models import Profile
#from rest_framework import viewsets
# from django.http import HttpResponseRedirect
# from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseNotFound
from Hall.models import hallPresence

from Login.models import Profile 
import datetime
# Create your views here.

# def login_view(request,*args,**kwargs):
    # profiles = Profile.objects.all()
    # # for pro in profiles:
    # #     print (pro.login)
    # #     if pro.login == True:
    # #         return redirect("../profile/")
    # if request.method == "POST" :
    #     user = request.POST.get('User ID')
    #     passw = request.POST.get('password')
    #     #pro = profile.ob
    #     #profiles = Profile.objects.all()
    #     userid=0
    #     for pro in profiles:
    #         userid=userid+1
    #         if pro.username == user and pro.password ==passw:
    #             pro.login = True
                
    #             return redirect("../profile/"+str(userid))
            
    #     #print(username+ " " + password)
    # return render(request,"login.html",{})

    # form = UserCreationForm()
    # return render(request,"login.html",{'form':form})
    
# def profile_view(request,id):
#     user=Profile.objects.get(id=id)
#     context={"username":user.username,"name":user.full_name}
#     return render(request,"profile.html",context)
@login_required
def profile_view(request):
    temp=datetime.date.today()
    result=temp-request.user.profile.last_logged_in
    print(result)
    request.user.profile.last_logged_in=temp
    
    if(request.user.profile.is_student==False):
        return HttpResponse("<h1>Page not found</h1>")
    return render(request,"profile.html")

@login_required
def dashboard_view(request):
    # obj=Profile.objects.get(roll_no=roll)
    # context={
    #     'Total_Price':obj.expense_total,
    #     'Last_Month':obj.expense_last_month,
    #     'Present_Month':obj.expense_current

    # }
    
    i=0
    count=hallPresence.objects.all().count()
    prime=0
    room=[]
    room.append("NA")
    room.append("NA")
    room.append("NA")
    time_enter=[]
    time_enter.append("NA")
    time_enter.append("NA")
    time_enter.append("NA")
    time_exit=[]
    time_exit.append("NA")
    time_exit.append("NA")
    time_exit.append("NA")

    while(count>0 and prime<3):
        object=hallPresence.objects.get(id=count)
        if (object.roll_no==request.user.profile.roll_no and object.in_hall==False):
            room[prime] = object.room_visiting
            time_enter[prime] = (object.timeEntered)
            time_exit[prime] = (object.timeExit)
            prime=prime+1
        count=count-1
    
    context={
        "Room_1":room[0],
        "Time_1":time_enter[0],
        "Time_exit_1":time_exit[0],
        "Room_2":room[1],
        "Time_2":time_enter[1],
        "Time_exit_2":time_exit[1],
        "Room_3":room[2],
        "Time_3":time_enter[2],
        "Time_exit_3":time_exit[2],
    }
            
    if(request.user.profile.is_student==False):
        return HttpResponse("<h1>Page not found</h1>")
    return render(request,"dashboard.html",context)

@login_required
def qrcode_view(request):
    if(request.user.profile.is_student==False):
        return HttpResponse("<h1>Page not found</h1>")
    return render(request,"qr_final.html")

@login_required
def logout_view(request):
    logout(request)
    return render(request,'logout.html')

@login_required
def check_view(request):
    if(request.user.profile.is_student==True):
        return redirect('../profile')
    
    elif (request.user.profile.is_staff==True):
        return redirect('../manager')
    
    else:
        return redirect('../security')
   