from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Revenues
from base.serializers import RevenuesSerializer

from rest_framework import status


@api_view(['GET'])
def getRevenue(request, pk):
    revenue = Revenues.objects.get(_id=pk)
    serializer = RevenuesSerializer(revenue, many=False)
    return Response(serializer.data)
