from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from ecommerce.Serializers import CartItemSerializer, CartSerializer, OrderItemSerializer, OrderSerializer, ProductSerializer

from .models import Cart, CartItem,Order, OrderItem, Product



class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer


class CartViewSet(viewsets.ModelViewSet):

    queryset = Cart.objects.all()

    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):

    queryset = CartItem.objects.all()

    serializer_class = CartItemSerializer

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()

    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = OrderItem.objects.all()

    serializer_class = OrderItemSerializer
