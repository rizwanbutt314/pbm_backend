from .models import BondCategory, BondDrawDates
from rest_framework import serializers

class BondCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BondCategory
        fields = '__all__'


class BondDrawDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BondDrawDates
        fields = '__all__'
