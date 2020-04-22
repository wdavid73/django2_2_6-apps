from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from confma.models import Client, Cloth, Cotizacion, Alquiler
from confma_api.serializers import ClientSerializer, ClothSerializer, CotizacionSerializer, RentalSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().filter(state=1)
    serializer_class = ClientSerializer


class ClientViewAPI(APIView):

    def get(self, request, pk, format=None):
        client = get_object_or_404(pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = ClientSerializer(client, context=serializer_context)
        return Response(serializer.data)


class ClothViewSet(viewsets.ModelViewSet):
    queryset = Cloth.objects.all().filter(state=1)
    serializer_class = ClothSerializer


class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizacion.objects.all().filter(state=1)
    serializer_class = CotizacionSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Alquiler.objects.all().filter(state=1)
    serializer_class = RentalSerializer
