from django.db import models


# customer model
class Customer(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    emails=models.EmailField()
    city=models.CharField(max_length=80)
    subcity=models.CharField(max_length=80)
    phonenum=models.IntegerField()

    def __str__(self) -> str:
        return self.firstname + self.lastname

class Apointment(models.Model):
    name = models.CharField(max_length=800)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    time=models.TimeField()
    people=models.IntegerField()
    message=models.TextField()


    def __str__(self) -> str:
        return self.name

class Package(models.Model):
    package_name = models.CharField(max_length=100)
    packimg=models.ImageField()
    package_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.package_name


class MenuCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(blank=True, null=True)
    menu_categories_pack = models.ForeignKey('Package', on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.category_name


class MenuItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_image = models.ImageField(upload_to='menu_items', null=True, blank=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='menu_items')
    packages = models.ForeignKey('Package', on_delete=models.CASCADE, related_name='menuitemspack')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name



# class Order(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     ordertype=models.CharField(max_length=50)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
#     package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, related_name='orders')
#     menu_items = models.ManyToManyField(MenuItem, related_name='orders')
#     menu_categories = models.ManyToManyField(MenuCategory, related_name='orders')
#     order_date = models.DateTimeField()
#     delivery_date = models.DateTimeField()
#     order_total = models.DecimalField(max_digits=10, decimal_places=2)
#     order_status = models.CharField(max_length=50, choices=[
#         ('pending', 'Pending'),
#         ('confirmed', 'Confirmed'),
#         ('in_progress', 'In Progress'),
#         ('delivered', 'Delivered'),
#         ('canceled', 'Canceled')
#     ])
#     payment_method = models.CharField(max_length=50, choices=[
#         ('telebirr', 'Telebirr'),
#         ('cash', 'Cash'),
#         ('bank_transfer', 'Bank Transfer')
#     ])
#     payment_status = models.CharField(max_length=50, choices=[
#         ('pending', 'Pending'),
#         ('paid', 'Paid'),
#         ('partially_paid', 'Partially Paid'),
#         ('refunded', 'Refunded')
#     ])
#     special_instructions = models.TextField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

  
#     def __str__(self):
#         return f"Order {self.order_id} - {self.customer.first_name} {self.customer.last_name}"

# class Menucategory_Order(models.Model):
#     category=models.ForeignKey(MenuCategory,on_delete=models.CASCADE)
#     orders=models.ForeignKey(Order,on_delete=models.CASCADE)


# class Menu_Order(models.Model):
#     menus=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
#     order=models.ForeignKey(Order,on_delete=models.CASCADE)


# class Driver(models.Model):
#     driver_fname = models.CharField(max_length=50)
#     driver_lname = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=20)
#     license_number = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.driver_fname} {self.driver_lname}"
    

# class CustomerFeedback(models.Model):
#     Cname=models.ForeignKey(Customer,on_delete=models.CASCADE)
#     packorder = models.OneToOneField(Package, on_delete=models.CASCADE, related_name='customer_feedback')
#     rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
#     comment = models.TextField()
#     date=models.DateTimeField()

#     def __str__(self) -> str:
#         return self.Cname
    

# class Request_for_Contact(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone = models.IntegerField()
#     comments = models.TextField(max_length=500)

#     def __str__(self) -> str:
#         return self.first_name + self.last_name


# class Apointment(models.Model):
#     first_name1 = models.CharField(max_length=50)
#     last_name1 = models.CharField(max_length=50)
#     email1 = models.EmailField()
#     phone1 = models.IntegerField()


#     def __str__(self) -> str:
#         return self.first_name1 + self.last_name1 