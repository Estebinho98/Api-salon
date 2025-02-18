from django.shortcuts import render
from rest_framework import generics
from .serializers import BuySerializer
from .models import Buy
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BuyView(generics.ListCreateAPIView):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer
    permission_classes = [IsAuthenticated]


class SingleBuyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer
    permission_classes = [IsAuthenticated]
