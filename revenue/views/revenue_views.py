from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from category.models import Revenue
from category.serializers import RevenueSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addRevenue(request):
    user = request.user
    data = request.data
    revenue = Revenue.objects.create(
        user=user,
        name=data['name'],
        price=data['price'],
    )
    serializer = RevenueSerializer(revenue, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRevenues(request):
    user = request.user
    revenues = Revenue.objects.filter(user=user)
    serializer = RevenueSerializer(revenues, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRevenueById(request, pk):
    user = request.user
    revenue = Revenue.objects.get(_id=pk, user=user)
    serializer = RevenueSerializer(revenue, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateRevenue(request, pk):
    user = request.user
    data = request.data
    revenue = Revenue.objects.get(_id=pk, user=user)
    revenue.name = data['name']
    revenue.price = data['price']
    revenue.save()
    serializer = RevenueSerializer(revenue, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteRevenue(request, pk):
    user = request.user
    revenueForDeletion = Revenue.objects.get(_id=pk, user=user)
    revenueForDeletion.delete()
    return Response('Revenue was deleted')

