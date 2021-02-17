from rest_framework.serializers import ModelSerializer
from mytig.models import ProductOnSale
from mytig.models import ProductAvailable

class ProductOnSaleSerializer(ModelSerializer):
    class Meta:
        model = ProductOnSale
        fields = ('id', 'tigID')


class ProductAvailableSerializer(ModelSerializer):
    class Meta:
        model = ProductAvailable
        fields = ('id', 'tigID')