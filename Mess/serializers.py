from dataclasses import fields
import imp
from rest_framework import serializers
from .models import messOrder,messMain,messExtras

class messOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = messOrder
        fields = '__all__'

class messMainSerializer(serializers.ModelSerializer):
    class Meta:
        model  = messMain
        fields = '__all__'

class messExtrasSerializer(serializers.ModelSerializer):
    class Meta:
        model  = messExtras
        fields = '__all__'
        