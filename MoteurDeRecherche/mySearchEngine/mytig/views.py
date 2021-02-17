import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from django.http import Http404
from rest_framework import renderers
import json
from rest_framework.reverse import reverse
from mytig.models import ProductOnSale
from mytig.models import ProductAvailable
from mytig.serializers import ProductOnSaleSerializer
from mytig.serializers import ProductAvailableSerializer


# Uncomment if images may iclude JPEG
class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data
# Uncomment if images may iclude PNG
class PNGRenderer(renderers.BaseRenderer):
    media_type = 'image/png'
    format = 'png'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


# Redirection Products
class RedirectionProductList(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)

class RedirectionProductDetail(APIView):
    def get_object(self, pk):
        try:
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
    def get(self, request, pk, format=None):
        response = requests.get(baseUrl+'product/'+str(pk)+'/')
        jsondata = response.json()
        return Response(jsondata)


# Products en pormotion
class OnSaleList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProductOnSale.objects.all():
            serializer = ProductOnSaleSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return Response(res)

class OnSaleDetail(APIView):
    def get_object(self, pk):
        try:
            return ProductOnSale.objects.get(tigID=pk)
        except ProductOnSale.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProductOnSaleSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)


# Products disponibles
class AvailableList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProductAvailable.objects.all():
            serializer = ProductAvailableSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return Response(res)

class AvailableDetail(APIView):
    def get_object(self, pk):
        try:
            return ProductAvailable.objects.get(tigID=pk)
        except ProductAvailable.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        prod = self.get_object(pk)
        serializer = ProductAvailableSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)


# Images
class ProductImageRandom(APIView):
    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, format=None):
        try:
            projectUrl = reverse('projectRoot',request=request, format=format)
            responseFromMyImageBank = requests.get(projectUrl+'myImageBank/random/')
            extractedUrl = json.loads(responseFromMyImageBank.text)['url']
            response = requests.get(extractedUrl)
            return Response(response)
        except:
            raise Http404

class ProductImage(APIView):
    renderer_classes = [JPEGRenderer,PNGRenderer]
    def get(self, request, pk, tigID, format=None):
        try:
            projectUrl = reverse('projectRoot',request=request, format=format)
            responseFromMyImageBank = requests.get(projectUrl+'myImageBank/'+str(tigID)+'/')
            extractedUrl = json.loads(responseFromMyImageBank.text)['url']
            response = requests.get(extractedUrl)
            return Response(response)
        except:
            raise Http404