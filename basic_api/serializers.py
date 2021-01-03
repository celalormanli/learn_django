from rest_framework import serializers
from basic_api.models import BasicApi


class BasicApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicApi
        fields = '__all__'
