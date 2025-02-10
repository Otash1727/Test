from rest_framework import serializers
from ..models import Organazation, PhoneNumber, Building, FoodType, CarsType, OtherProductType

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['id', 'phone_number', 'created_at']

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ['id', 'address', 'latitude', 'longitude', 'created_at']

class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['id', 'title']

class CarsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsType
        fields = ['id', 'title']

class OtherProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherProductType
        fields = ['id', 'title']

# New Serializer to include all related data in one JSON response
class OrganizationDetailSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(source='phonenumber_set', many=True)
    buildings = BuildingSerializer(source='building_set', many=True)
    food_type = FoodTypeSerializer(source='food_types', many=True)  # Fixed
    car_type = CarsTypeSerializer(source='car_types', many=True)  # Fixed
    other_product_type = OtherProductTypeSerializer(source='other_product_types', many=True)  # Fixed

    class Meta:
        model = Organazation
        fields = ['id', 'title', 'token', 'phone_numbers', 'buildings', 'food_type', 'car_type', 'other_product_type']
