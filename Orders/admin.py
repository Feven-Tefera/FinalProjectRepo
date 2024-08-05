from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CartItem)
admin.site.register(Checkout)
admin.site.register(Payment)
admin.site.register(DeliveryInfo)
admin.site.register(Driver)