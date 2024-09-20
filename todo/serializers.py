from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class TodoSerializer(ModelSerializer):
    
    
    class Meta:
        model = Todo
        fields = '__all__'
        
        

    