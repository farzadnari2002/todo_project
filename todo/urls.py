from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


app_name = 'todos'

router = DefaultRouter()

router.register('categorys', CategoryApiVIew)

router.register('', TodoApiView)

urlpatterns = [
    path('', include(router.urls), name='api'),
    
]
