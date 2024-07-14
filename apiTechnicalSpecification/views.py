from rest_framework import generics
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Equipment, EquipmentType
from .serializers import EquipmentSerializer, EquipmentTypeSerializer


class EquipmentPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class EquipmentApiList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    pagination_class = EquipmentPagination


class EquipmentTypeApiList(generics.ListCreateAPIView):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer
    pagination_class = EquipmentPagination


class EquipmentApiUpdate(generics.UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentTypeApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer


class EquipmentApiView(APIView):
    def get(self, request):
        _equipment = Equipment.objects.all()
        return Response({'posts': EquipmentSerializer(_equipment, many=True).data})

    def post(self, request):
        serializer = EquipmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT is not allowed"})
        try:
            instance = Equipment.objects.get(pk=pk)
        except:
            return Response({"objects": "Object does not exists"})

        serializer = EquipmentSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE is not allowed"})

        return Response({"post": "delete post " + str(pk)})
