from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib.auth.decorators import login_required
from .models import *
from cateringAPP.models import *
from cateringAPP.views import *
import logging
from decimal import Decimal

@login_required
def cart_view(request):
    user = request.user
    customer = get_object_or_404(Customer, user=user)

    cart_items = CartItem.objects.filter(user_account=customer).select_related('package', 'menu_item')

    total_price = sum(
        (item.package.package_price * item.quantity) if item.package else Decimal('0.00')
        for item in cart_items
    )
    
    shipping_cost = Decimal('5000.00')
    tax = total_price * Decimal('0.15')
    total_cost = total_price + shipping_cost + tax

    selected_package = request.session.get('selected_package')
    logger.debug("Selected package retrieved from session: %s", selected_package)

    # Calculate the total including the package price if selected
    if selected_package:
        package_price = Decimal(selected_package['package_price'])
        total_cost += package_price  # Add package price to the total cost
        total_price += package_price   # Add package price to the total price

    context = {
        'cart_items': cart_items,
        'customer': customer,
        'total_price': total_price,
        'shipping_cost': shipping_cost,
        'tax': tax,
        'total_cost': total_cost,
        'selected_package': selected_package,  
    }

    return render(request, 'carts.html', context)





@login_required
def select_package(request):
    if request.method == 'POST':
        package_id = request.POST.get('package_id')
        package = get_object_or_404(Package, id=package_id)

        request.session['selected_package'] = {
            'package_id': package.id,
            'package_name': package.package_name,
            'package_price': str(package.package_price),  
        }
        
        logger.debug("Selected package stored in session: %s", request.session['selected_package'])

        return redirect('cateringAPP:food')  

    packageformitems = Package.objects.all() 
    return render(request, 'index.html', {'packageformitems': packageformitems})



logger = logging.getLogger(__name__)

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        logger.debug("POST data: %s", request.POST)

        user = request.user
        customer = get_object_or_404(Customer, user=user)

        selected_menu_items = request.POST.getlist('menu_items')
        logger.debug("Selected menu items: %s", selected_menu_items)

        # Add selected menu items to cart
        for menu_item_id in selected_menu_items:
            if menu_item_id:
                menu_item = get_object_or_404(MenuItem, item_id=menu_item_id)
                cart_item, created = CartItem.objects.get_or_create(
                    user_account=customer,
                    menu_item=menu_item,
                    defaults={'quantity': 1}
                )
                if not created:
                    cart_item.quantity += 1
                    cart_item.save()

        # Handle selected package
        selected_package = request.session.get('selected_package')
        if selected_package:
            package = get_object_or_404(Package, id=selected_package['package_id'])
            cart_item, created = CartItem.objects.get_or_create(
                user_account=customer,
                package=package,
                defaults={'quantity': 1}
            )
            if not created:
                cart_item.quantity += 1
                cart_item.save()

            # Clear the session variable for the selected package
            # del request.session['selected_package']

        return redirect('Orders:cart_view')

    return redirect('cateringAPP:food')



@login_required
def remove_from_cart(request, item_id):
    user = request.user
    customer = get_object_or_404(Customer, user=user)
    cart_item = get_object_or_404(CartItem, id=item_id, user_account=customer)
    cart_item.delete()
    messages.success(request, 'Item removed from cart successfully.')

    return redirect('Orders:cart_view')