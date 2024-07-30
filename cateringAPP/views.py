from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import *
from .forms import *
from django.urls import reverse
# Create your views here.

def index(request):
   apointment_list = Apointment.objects.all()
   packageformitems=Package.objects.all()
  
   data ={
        'apointment_list':apointment_list, 'packageformitems':packageformitems
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
    categories = MenuCategory.objects.all()
    menu_items = MenuItem.objects.all()

    data = {
        'categories': categories,
        'menu_items': menu_items,
    }

    return render(request, 'foods.html', data)

def cart_view(request):
    data={}
    return render(request,'carts.html',data)


# def get_menu_items(request, category_id):
#     try:
#         category = MenuCategory.objects.get(id=category_id)
#         menu_items = MenuItem.objects.filter(category=category)
#         menu_items_data = [
#             {
#                 'item_name': menu_item.item_name,
#                 'item_description': menu_item.item_description,
#                 'item_image': menu_item.item_image.url if menu_item.item_image else '',
#                 'price': menu_item.packages.first().price,  # Assuming each MenuItem has at least one Package
#             }
#             for menu_item in menu_items
#         ]
#         return JsonResponse(menu_items_data, safe=False)
#     except MenuCategory.DoesNotExist:
#         return JsonResponse({'error': 'Category not found'}, status=404)





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
    categoryformitems = MenuCategory.objects.all()
    menuformitems =MenuItem.objects.all()
    return render(request, 'tables.html', {'packageformitems': packageformitems,'categoryformitems':categoryformitems, 'menuformitems':menuformitems})

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

def menu_cat_view(request):
    categoryformitems = MenuCategory.objects.all()
    category_form = Menucatform(request.POST or None, request.FILES or None)
    if category_form.is_valid():
        category_form.save()
        return redirect('menucategory')
    data = {
        'category_form': category_form,
        'categoryformitems': categoryformitems
    }
    return render(request, 'dashmenucategory.html', data)

def menu_view(request):
    menuformitems =MenuItem.objects.all()
    menu_form =menuForm(request.POST or None, request.FILES or None)
    if menu_form.is_valid():
        menu_form.save()
        return redirect('menus')
    data={
          'menu_form':menu_form,
         'menuformitems':menuformitems
    }
    return render(request,'dashmenu.html',data)






