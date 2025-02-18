from rest_framework import serializers
from .models import Servicies
from CategoriaApp.serializers import CategorySerializer

class ServiciesSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)


    class Meta:
        model = Servicies
        fields = ['id','title','price','description','category','category_id']
