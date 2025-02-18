from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import ProductsSerilizer
from .models import Products
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle 
# Create your views here.

class ProductsView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerilizer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    ordering_fields = ['price', 'inventory','title']
    filterset = ['price', 'category']
    search_fields = ['category__title']

class SingleProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerilizer
    permission_classes = [IsAuthenticated]

