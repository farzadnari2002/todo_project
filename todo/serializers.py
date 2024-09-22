from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class TodoSerializer(ModelSerializer):
    Category = CategorySerializer(read_only=True, many=True)
    
    class Meta:
        model = Todo
        fields = '__all__'
        
        

    