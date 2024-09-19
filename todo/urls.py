from django.urls import path
from .views import *


app_name = 'todos'

urlpatterns = [
    path('', TodoListApiView.as_view(), name='list'),
    path('<int:pk>', TodoDetailApiView.as_view(), name='detail'),
]
