from django.contrib import admin
from .models import Item, Category, User, Order, OrderItem, Profile, Bug, Comment

# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Bug)
admin.site.register(Comment)
