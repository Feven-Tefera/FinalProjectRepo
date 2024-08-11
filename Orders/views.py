from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect,render
from django.contrib.auth.decorators import login_required
from .models import *
from cateringAPP.models import *
from cateringAPP.views import *
import logging

@login_required
def cart_view(request):
    user = request.user
    logger.debug(f"Logged in user: {user}")

    customer = Customer.objects.filter(user=user).first()

    if customer is None:
        return render(request, 'error.html', {'message': 'Customer not found.'})

    cart_items = CartItem.objects.filter(user_account=customer).select_related('menu_item', 'package')

    # Calculate total costs using package prices
    total_price = sum(
        (item.package.package_price * item.quantity) if item.package else 0
        for item in cart_items
    )
    
    shipping_cost = 5000.00  
    tax = total_price * 0.15  
    total_cost = total_price + shipping_cost + tax

    context = {
        'cart_items': cart_items,
        'customer': customer,
        'total_price': total_price,
        'shipping_cost': shipping_cost,
        'tax': tax,
        'total_cost': total_cost,
    }

    return render(request, 'carts.html', context)




logger = logging.getLogger(__name__)
@login_required
def add_to_cart(request):
    if request.method == 'POST':
        logger.debug("POST data: %s", request.POST)

        user = request.user
        customer = get_object_or_404(Customer, user=user)

        selected_menu_items = request.POST.getlist('menu_items')
        logger.debug("Selected menu items: %s", selected_menu_items)

        # Add selected menu items to the cart
        for menu_item_id in selected_menu_items:
            if menu_item_id:  # Ensure the ID is not empty
                menu_item = get_object_or_404(MenuItem, item_id=menu_item_id)  # Use item_id
                cart_item, created = CartItem.objects.get_or_create(
                    user_account=customer,
                    menu_item=menu_item,
                    defaults={'quantity': 1}
                )
                if not created:
                    cart_item.quantity += 1
                    cart_item.save()

        # Handle packages similarly (if needed)
        selected_package_id = request.POST.get('package_id')
        if selected_package_id:
            package = get_object_or_404(Package, id=selected_package_id)
            cart_item, created = CartItem.objects.get_or_create(
                user_account=customer,
                package=package,
                defaults={'quantity': 1}
            )
            if not created:
                cart_item.quantity += 1
                cart_item.save()

        return redirect('Orders:cart_view')

    return redirect('cateringAPP:food')