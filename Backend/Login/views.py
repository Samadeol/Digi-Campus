from django.shortcuts import render, redirect
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework import viewsets
# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('full_name')
    serializer_class = ProfileSerializer

def login_view(request,*args,**kwargs):
    if request.method == "POST" :
        user = request.POST.get('User ID')
        passw = request.POST.get('password')
        #pro = profile.ob
        profiles = Profile.objects.all()
        for pro in profiles:
            if pro.username == user and pro.password ==passw :
                return redirect("../mess/")
        #print(username+ " " + password)
    return render(request,"login.html",{})