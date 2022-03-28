from dataclasses import fields
import imp
from rest_framework import serializers
from .models import hallPresence

class hallPresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = hallPresence
        fields = '__all__'