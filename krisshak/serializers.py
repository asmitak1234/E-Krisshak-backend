# <!-- Made By - Asmita Kumari -->

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Krisshak
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        # Check for length
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        
        # Check for at least one letter, one number, and one special character
        if (not re.search(r'[A-Za-z]', value) or
            not re.search(r'[0-9]', value) or
            not re.search(r'[@$!%*#?&]', value)):
            raise serializers.ValidationError(
                "Password must contain at least one letter, one number, and one special character."
            )

        return value

    def create(self, validated_data):
        # print(validated_data)
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