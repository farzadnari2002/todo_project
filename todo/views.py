from django.shortcuts import render
from .models import *
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination


class CategoryApiViewPagination(LimitOffsetPagination):
    page_size = 6


class TodoApiView(ModelViewSet):
    queryset = Todo.objects.order_by('priority').all()
    serializer_class = TodoSerializer

    
    
class CategoryApiVIew(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryApiViewPagination
        
        
        

