from django.shortcuts import render
from cateringAPP.models import Customer
# Create your views here.

def login_view(request):
    
    return render(request,'login.html')

def signup_view(request):
    return render(request,'signup.html')