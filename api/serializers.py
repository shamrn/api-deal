from rest_framework import serializers
from .models import DealData


class FileCsvSerialiser(serializers.ModelSerializer):
    class Meta:
        model = DealData
        fields = ('username', 'spent_money', 'gems')
