from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def cart_view(request):
    
    data={}
    
    
    return render(request,'carts.html',data)
