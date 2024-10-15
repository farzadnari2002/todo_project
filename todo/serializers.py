from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

        
class TodoSerializer(ModelSerializer):
    
    def validate_priority(self, priority):
        if priority == 0:
            raise serializers.ValidationError('not can 0')
        return priority
    
    class Meta:
        model = Todo
        fields = '__all__'
        
        
class CategorySerializer(ModelSerializer):
    todos = TodoSerializer(read_only=True, many=True)
    
    class Meta:
        model = Category
        fields = '__all__'
    
        


        

    