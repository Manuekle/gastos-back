from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from category.models import Categories
from category.serializers import CategorySerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCategory(request):
    user = request.user
    data = request.data
    category = Categories.objects.create(
        user=user,
        name=data['name'],
        price=data['price'],
    )
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCategories(request):
    user = request.user
    categories = Categories.objects.filter(user=user)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCategoryById(request, pk):
    user = request.user
    category = Categories.objects.get(_id=pk, user=user)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCategory(request, pk):
    user = request.user
    data = request.data
    category = Categories.objects.get(_id=pk, user=user)
    category.name = data['name']
    category.price = data['price']
    category.save()
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCategory(request, pk):
    user = request.user
    categoryForDeletion = Categories.objects.get(_id=pk, user=user)
    categoryForDeletion.delete()
    return Response('Category was deleted')

