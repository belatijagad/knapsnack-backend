from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth import get_user_model, authenticate

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

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    user = get_user_model().objects.create_user(
        username = request.data['username'],
        password = request.data['password'],
    )

    token, _ = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key})

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)

    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials.'}, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_consumables(request):
    consumables = Consumable.objects.all()
    serializer = ConsumableSerializer(consumables, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_consumable(request, pk):
    consumable = Consumable.objects.get(id=pk)
    serializer = ConsumableSerializer(consumable, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
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