from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
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

def package_view(request):
    packageformitems = Package.objects.all()
    package_form = PackageForm(request.POST or None, request.FILES or None)
    if package_form.is_valid():
        package_form.save()
        return redirect('packages')

    data = {
        'form': package_form,
        'packageformitems': packageformitems
    }
    return render(request, 'packagesdetailsall.html', data)

def tables_view(request):
    packageformitems = Package.objects.all()
    return render(request, 'tables.html', {'packageformitems': packageformitems})

def package_edit_view(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            return redirect('tables')
    else:
        form = PackageForm(instance=package)
    return render(request, 'package_edit.html', {'form': form, 'package': package})

def package_delete_view(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        package.delete()
        return redirect('tables')
    return render(request, 'package_delete.html', {'package': package})
