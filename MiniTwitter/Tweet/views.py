from django.shortcuts import render

from rest_framework import viewsets

from .models import Tweet
from .serializers import TweetModelSerializer

class TweetModelViewSet(viewsets.ModelsViewSet):
    serializer_class = TweetModelSerializer
    queryset = Tweet.objects.all()
    


# Create your views here.
