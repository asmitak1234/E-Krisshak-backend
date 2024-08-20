# <!-- Made By - Asmita Kumari -->

from rest_framework import serializers
from .models import Krisshak

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
               )