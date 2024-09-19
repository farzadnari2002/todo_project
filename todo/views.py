from django.shortcuts import render
from .models import Todo
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework import generics, mixins


class TodoListApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer
    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)
        

class TodoDetailApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request)
    
    def put(self, request: Request, pk):
        return self.update(request)
    
    def delete(self, request: Request, pk):
        return self.destroy(request)
    
    
        
        
        

