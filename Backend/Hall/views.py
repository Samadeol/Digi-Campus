from asyncio.windows_events import NULL
from django.shortcuts import render

from Hall.models import hallPresence
from .form import EntryForm
from .form import ExitForm
# Create your views here.
import datetime
from django.contrib.auth.models import User
def entry_view(request):
    if request.method == "POST":
        MyLoginForm = EntryForm(request.POST or None)
        if MyLoginForm.is_valid():
            user_visiting = MyLoginForm.cleaned_data['user_visiting']
            laptop=MyLoginForm.cleaned_data['laptop']
            time=datetime.datetime.now()
            user_in=0
            l=False
            if(laptop=='Yes'):
                l=True
            for x in hallPresence.objects.all():
                if (str(x.user) == str(request.user.username) and x.in_hall == True):
                    user_in=1
            
            if user_in==0:
                z=hallPresence(user=request.user,user_visiting=int(user_visiting),in_hall=True,laptop=l,timeEntered=time)
                z.save()

    else:
        MyLoginForm = EntryForm(request.POST or None)
    context = {"form": MyLoginForm}
    return render(request, "entry.html", context)


def exit_view(request):
    if request.method == "POST":
        time=datetime.datetime.now()
        for x in hallPresence.objects.all():
            if str(x.user) == str(request.user.username):
                if(x.in_hall==True):
                    x.in_hall=False
                    x.timeExit=time
                    x.save()                    

            

    # else:
    #     MyLogoutForm = ExitForm(request.POST or None)
    # context = {"form": MyLogoutForm}
    return render(request, "exit.html", {})