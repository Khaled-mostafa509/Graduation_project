from rest_framework import serializers
from .models import Home

class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'