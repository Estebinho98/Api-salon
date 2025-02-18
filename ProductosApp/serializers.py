from rest_framework import serializers 
from .models import Products
from CategoriaApp.serializers import CategorySerializer

class ProductsSerilizer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)


    class Meta:
        model = Products
        fields = ['id','title','price','inventory','description','category','category_id']