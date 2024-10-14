from django.shortcuts import render
from  django.http import HttpResponse
from myapp.forms import loginform
 
# Create your views here.
 
 
def index(req):
    if(req.method=="POST"):
        databasedata= loginform(req.POST)
        databasedata.save()
        return HttpResponse("Data Added Successfully")
    form = loginform()
    return render(req,'index.html',{'form':form})
 
 


