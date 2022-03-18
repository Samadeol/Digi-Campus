from django.shortcuts import render

# Create your views here.
def entry_view(request):
    return render(request,"entry.html")