from rest_framework.serializers import ModelSerializer
from myImageBank.models import ImageProduct
from myImageBank.models import ImageProductMeta

class ImageProductSerializer(ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = ('id', 'url', 'metadata')

class ImageProductMetaSerializer(ModelSerializer):
    class Meta:
        model = ImageProductMeta
        fields = ('id', 'keyword', 'idList')
