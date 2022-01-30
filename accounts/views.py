from django.shortcuts import redirect ,render
from .forms import SignupForm
from django.contrib.auth import authenticate ,login


# from .models import accounts

# Create your views here.


def signup(request):
    if request.method== "Post":
        form= SignupForm(request.POST)
        if form is valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        SignupForm()
    
    return render(request,'registration/signup.html',{'form':form})
