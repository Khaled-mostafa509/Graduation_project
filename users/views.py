from django.shortcuts import render
from .models import Home
# Create your views here.

def Home_list(request):
    Home_list= Home.objects.all()
    context={'Home':Home_list}
    return render(request,'Home/Home_list.html',context)


def Home_details(request,id ):
    pass
