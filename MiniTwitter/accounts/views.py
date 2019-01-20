from django.shortcuts import render
from rest_framework import viewsets
from .models import MyUser

from .serializers import MyUserMModelSerializer
# Create your views here.

class MyUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = MyUserMModelSerializer
    queryset = MyUser.objects.all().order_by('-username')

