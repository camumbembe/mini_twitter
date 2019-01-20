from rest_framework import serializers

from .models import MyUser

class MyUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fiels = ('username', 'email', 'password', 'following')