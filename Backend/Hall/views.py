from django.shortcuts import render
from .form import EntryForm
# Create your views here.
def entry_view(request):
    form=EntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=EntryForm()
    context={'form':form}
    return render(request,"entry.html",context)