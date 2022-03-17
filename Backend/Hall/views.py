from django.shortcuts import render

def hall_entry(request):
    return render(request,"hall.html",{})