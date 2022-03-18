from django.shortcuts import render
from .form import EntryForm
# Create your views here.


def entry_view(request):
    # form=EntryForm(request.POST or None)

    # if form.is_valid():
    #     form.save()
    #     form=EntryForm()
    # context={'form':form}
    if request.method == "POST":
        MyLoginForm = EntryForm(request.POST)
        if MyLoginForm.is_valid():
            user_visiting = MyLoginForm.cleaned_data['user_visiting']
            laptop = MyLoginForm.cleaned_data['laptop']
            print(laptop)
            print(user_visiting)
    else:
        MyLoginForm = EntryForm()
    context = {"form": MyLoginForm}
    return render(request, "entry.html", context)
