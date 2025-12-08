from django.contrib import admin

# Register your models here.
from .models import Product, Customer, Address, Order

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Order)