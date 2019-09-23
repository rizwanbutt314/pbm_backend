from .models import BondCategory
from rest_framework import serializers

class BondCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BondCategory
        fields = '__all__'
