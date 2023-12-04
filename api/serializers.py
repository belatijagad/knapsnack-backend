from rest_framework import serializers
from .models import Consumable, CustomUser, Review

class ConsumableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumable
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields= '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        consumable = validated_data['consumable']

        if Review.objects.filter(user=user, consumable=consumable).exists():
            raise serializers.ValidationError('You have already reviewed this food!')

        return Review.objects.create(**validated_data)