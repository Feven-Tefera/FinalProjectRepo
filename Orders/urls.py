from django.urls import path
from .views import add_to_cart , cart_view

app_name = 'Orders'

urlpatterns = [
    path('cart/', cart_view, name='cart_view'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),  
]

