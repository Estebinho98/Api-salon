from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import ServiciesSerializer
from .models import Servicies
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class ServiciesView(viewsets.ModelViewSet):
    queryset = Servicies.objects.all()
    serializer_class = ServiciesSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['price', 'title']
    filterset = ['price', 'category']
    search_fields = ['category__title']


# class SingleServicieView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Servicies.objects.all()
#     serializer_class = ServiciesSerializer
#     permission_classes = [IsAuthenticated]
