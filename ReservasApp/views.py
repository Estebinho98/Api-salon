from django.shortcuts import render
from rest_framework import generics
from .serializers import BookingsSerializer
from .models import Bookings
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BookingsView(generics.ListCreateAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [IsAuthenticated]


class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [IsAuthenticated]
