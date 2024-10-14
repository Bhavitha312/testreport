from django.shortcuts import render
from  django.http import HttpResponse
from myapp.forms import loginform
from myapp.models import User
from django.contrib import messages
 
# Create your views here.
 
 
def index(req):
    if(req.method=="POST"):
        databasedata= loginform(req.POST)
        databasedata.save()
        return HttpResponse("Data Added Successfully")
    form = loginform()
    return render(req,'index.html',{'form':form})
 
 
def login_view(req):
    if req.method=="POST":
        name= req.POST.get('name')
        passw= req.POST.get('password')
 
        try:
            user=User.objects.get(name=name,password=passw)
            return HttpResponse("Login Successfully")
        except User.DoesNotExist:
            messages.error(req,"Invalid username or password")
            return render(req,'login.html')
    form = loginform()
    return render(req,'login.html',{'form':form})
 
 
 
 


