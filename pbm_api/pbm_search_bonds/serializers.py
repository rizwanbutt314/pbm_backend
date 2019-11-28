from rest_framework import serializers

class SearchBondSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=10)
    date = serializers.CharField(max_length=15)
    searchtype = serializers.CharField(max_length=50)
    file = serializers.CharField(required=False, default='')
    range = serializers.CharField(required=False, default='')
    numbers = serializers.CharField(required=False, default='')
