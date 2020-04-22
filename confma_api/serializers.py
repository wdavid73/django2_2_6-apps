from rest_framework import serializers
from confma.models import Cloth, Client, Cotizacion, Alquiler, CotizacionClient


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="confma_api:client-detail")

    class Meta:
        model = Client
        fields = ['url', 'id', 'name', 'lastname', 'address', 'phone', 'cellphone']


class ClothSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="confma_api:cloth-detail")

    class Meta:
        model = Cloth
        fields = ['url', 'id', 'name', 'color', 'size', 'fashion', 'image']


class CotizacionSerializer(serializers.HyperlinkedModelSerializer):
    cloth = serializers.HyperlinkedIdentityField(view_name="confma_api:cloth-detail")
    client = serializers.HyperlinkedIdentityField(view_name="confma_api:client-detail")

    class Meta:
        model = Cotizacion
        fields = ['url',
                  'id',
                  'value_cloth',
                  'value_work',
                  'value_threads',
                  'value_buttons',
                  'value_necks',
                  'value_embroidery',
                  'value_prints',
                  'cloth',
                  'client']


class RentalSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="confma_api:alquiler-detail", lookup_field='id')
    cloth = serializers.HyperlinkedIdentityField(view_name="confma_api:cloth-detail", lookup_field='cloth_id')
    client = serializers.HyperlinkedIdentityField(view_name="confma_api:client-detail", lookup_field='client_id')

    class Meta:
        model = Alquiler
        fields = ['url', 'id', 'date_return', 'price', 'cloth', 'client']


class CotizacionClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CotizacionClient
        fields = ['url', 'id', 'cotizacion', 'client', 'total']
