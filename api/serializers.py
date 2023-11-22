from rest_framework.serializers import ModelSerializer
from .models import Consumable

class ConsumableSerializer(ModelSerializer):
    class Meta:
        model = Consumable
        fields = '__all__'