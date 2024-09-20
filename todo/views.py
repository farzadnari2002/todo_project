from django.shortcuts import render
from .models import Todo
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


class TodoApiView(ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

        
        
        

