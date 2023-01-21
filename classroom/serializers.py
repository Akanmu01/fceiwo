from rest_framework import serializers
from .models import *

class AdmissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Admission
        fields = '__all__'

