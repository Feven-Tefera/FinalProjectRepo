from django.urls import path
from .views import add_to_cart , cart_view,select_package,remove_from_cart

app_name = 'Orders'

urlpatterns = [
    path('cart/', cart_view, name='cart_view'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),  
    path('select-package/', select_package, name='select_package'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]

