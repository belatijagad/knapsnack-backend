from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ConsumableSerializer
from .models import Consumable

@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/',
            'method': '',
            'body': '',
            'description': '',
        }
    ]

    return Response(routes)

@api_view(['GET'])
def get_consumables(request):
    consumables = Consumable.objects.all()
    serializer = ConsumableSerializer(consumables, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_consumable(request, pk):
    consumable = Consumable.objects.get(id=pk)
    serializer = ConsumableSerializer(consumable, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_consumable(request):
    data = request.data
    consumable = Consumable.objects.create(
        name = data['name'],
        description = data['description'],
        price = data['price'],
    )
    serializer = ConsumableSerializer(consumable, many=False)

    return Response(serializer.data)

@api_view(['PUT'])
def update_consumable(request, pk):
    data = request.data
    
    consumable = Consumable.objects.get(id=pk)
    serializer = ConsumableSerializer(consumable, data=data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_consumable(request, pk):
    data = request.data
    
    consumable = Consumable.objects.get(id=pk)
    consumable.delete()
    
    return Response("Consumable was deleted!")