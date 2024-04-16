from django.contrib import admin
from .models import CartItem, OrderItem, Product, Cart, Order

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(OrderItem)