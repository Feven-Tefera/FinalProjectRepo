from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
   apointment_list = Apointment.objects.all()
   data ={
        'apointment_list':apointment_list
    }
   if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        date =request.POST.get('date')
        time=request.POST.get('time')
        people=request.POST.get('people')
        message=request.POST.get('message')
      
        obj=Apointment()
        obj.name=name
        obj.email=email
        obj.phone=phone
        obj.date=date
        obj.time=time
        obj.people=people
        obj.message=message
        obj.save()
   
   return render(request,'index.html',data)
def food(request):
    data={

    }
    return render(request,'foods.html',data)
def dashboard_view(reqest):
    data={}
    return render(reqest,'dashboard.html',data)

def Appointemnt_view(request):
   apointment_list = Apointment.objects.all()
   data ={
        'apointment_list':apointment_list
    }
   if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        phone =request.POST.get('phone')
        date =request.POST.get('date')
        time=request.POST.get('time')
        people=request.POST.get('people')
        message=request.POST.get('message')
      
        obj=Apointment()
        obj.name=name
        obj.email=email
        obj.phone=phone
        obj.date=date
        obj.time=time
        obj.people=people
        obj.message=message
        obj.save()
   return render(request,'Appointmentdashboard.html',data)