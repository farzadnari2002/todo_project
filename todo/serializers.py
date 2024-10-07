from rest_framework.serializers import ModelSerializer
from .models import *

        
class TodoSerializer(ModelSerializer):
    
    class Meta:
        model = Todo
        fields = '__all__'
        
        
class CategorySerializer(ModelSerializer):
    todos = TodoSerializer(read_only=True, many=True)
    
    class Meta:
        model = Category
        fields = '__all__'
    
        


        

    