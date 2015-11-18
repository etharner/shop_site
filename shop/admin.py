from django.contrib import admin
from .models import Item, Category, User, Order, OrderItem

# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)
