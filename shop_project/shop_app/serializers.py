from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from . models import ProductName

class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductName
        fields = '__all__'