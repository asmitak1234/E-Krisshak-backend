# <!-- Made By - Asmita Kumari -->

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Krisshak

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    
    
class KrisshakSerializer(serializers.ModelSerializer):
    class Meta:
        model=Krisshak
        fields=('krisshakId',
                'FirstName',
                'LastName',
                'Address',
                'Email',
                'RegistrationNo',
                'Age',
                'Experience',
                'MasteryGrow',
                'HighestEducation',
                'author',
               )
        extra_kwargs = {"author": {"read_only": True}}