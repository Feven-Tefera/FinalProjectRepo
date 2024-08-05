import uuid
from django.db import models
from cateringAPP.models import*

class CartItem(models.Model):
    user_account = models.ForeignKey(Customer, related_name='cart_items', on_delete=models.CASCADE)
    package = models.ForeignKey(Package, related_name='cart_items', on_delete=models.CASCADE, null=True, blank=True)
    menu_item = models.ForeignKey(MenuItem, related_name='cart_items', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)  # Set a default quantity

    def __str__(self):
        return self.user_account


class Checkout(models.Model):
    cart_item = models.ForeignKey(CartItem, related_name='checkouts', on_delete=models.CASCADE)
    package_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounts = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    price_off = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, default='pending')  # e.g., pending, completed, canceled
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Checkout {self.id} - Status: {self.status}"

    def mark_as_completed(self):
        self.status = 'completed'
        self.save()


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('chapa', 'Chapa'),
    ]

    checkout = models.OneToOneField(Checkout, related_name='payment_info', on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique order ID
    invoice_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique invoice number
    user_account = models.ForeignKey(Customer, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount paid
    payment_date = models.DateTimeField(auto_now_add=True)  # Automatically set the date on creation
    payment_status = models.CharField(max_length=20, default='pending')  # e.g., pending, completed, failed
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)  # Payment method

    def __str__(self):
        return f"Payment {self.invoice_number} - Status: {self.payment_status}"



class DeliveryInfo(models.Model):
    checkout = models.OneToOneField(Checkout, related_name='delivery_info', on_delete=models.CASCADE)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    address = models.CharField(max_length=255)
    delivery_time = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='pending')  # e.g., pending, dispatched, delivered

    def __str__(self):
        return f"Delivery to {self.address} - Status: {self.status}"


class Driver(models.Model):
    full_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    checkouts = models.ManyToManyField(Checkout, related_name='drivers', blank=True)
    delivery_info = models.ManyToManyField(DeliveryInfo, related_name='drivers', blank=True)

    def __str__(self):
        return self.full_name
