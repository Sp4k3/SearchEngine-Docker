from rest_framework.views import APIView
from rest_framework.response import Response
from myImageBank.config import randomImageUrl
from django.http import Http404
from mytig.config import baseUrl
import secrets
import random
from django.db.models import Q

from myImageBank.models import ImageProduct
from myImageBank.models import ImageProductMeta
from myImageBank.serializers import ImageProductSerializer
from myImageBank.serializers import ImageProductMetaSerializer

# Images
class ImageList(APIView):
    def get_object(self):
        try:
            return ImageProduct.objects.all()
        except ImageProduct.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        print('test')
        images = self.get_object()
        res = []
        for image in self.get_object():
            serializer = ImageProductSerializer(image)
            res.append(serializer.data)
        return Response(res)

class RandomImage(APIView):
    def get_object(self):
        try:
            rand = random.randint(0, len(randomImageUrl) - 1)
            return ImageProduct.objects.get(id=rand)
        except ImageProduct.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        prod = self.get_object()
        serializer = ImageProductSerializer(prod)
        return Response(serializer.data)

class Image(APIView):
    def get_object(self, pk):
        try:
            return ImageProduct.objects.get(id=pk)
        except ImageProduct.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ImageProductSerializer(image)
        return Response(serializer.data)

# class ImagesByName(APIView):
#     def get_object(self, name):
#         try:
#             return ImageProduct.objects.all().filter(metadata__contains="'" + name + "'")
#         except ImageProduct.DoesNotExist:
#             raise Http404
#     def get(self, request, name, format=None):
#         res = []
#         for image in self.get_object(name):
#             serializer = ImageProductSerializer(image)
#             res.append(serializer.data)
#         return Response(res)

class ImagesByName(APIView):
    def get_object(self, name):
        if ' ' in name:
            keywords = name.split(' ')
            q = Q()
            for i in range(len(keywords)):
                keyword = ImageProductMeta.objects.get(keyword=keywords[i])
                serializer = ImageProductMetaSerializer(keyword)
                idList = serializer.data['idList'].split(',')
                q &= Q(id__in=idList)
        else:
            keyword = ImageProductMeta.objects.get(keyword=name)
            serializer = ImageProductMetaSerializer(keyword)
            idList = serializer.data['idList'].split(',')
            q = Q(id__in=idList)
        try:
            imageList = ImageProduct.objects.filter(q)
            # imageList = ImageProduct.objects.filter(q).extra(order_by=[Length('metadata')]) 
            # print(ImageProduct.objects.filter(q).order_by(str('metadata').index("red"))) 
            print(idList)
            return imageList
        except ImageProduct.DoesNotExist:
            raise Http404
    def get(self, request, name, format=None):
        res = []
        for image in self.get_object(name):
            serializer = ImageProductSerializer(image)
            res.append(serializer.data)
        return Response(res)


class ImagesByRegex(APIView):
    def get_object(self, name):
        try:
            keywords = ImageProductMeta.objects.filter(keyword__regex=name)
            q = Q()
            for i in range(len(keywords)):
                serializer = ImageProductMetaSerializer(keywords[i])
                idList = serializer.data['idList'].split(',')
                q |= Q(id__in=idList)
                print(idList)
            imageList = ImageProduct.objects.filter(q)
            return imageList
        except ImageProduct.DoesNotExist: 
            raise Http404
    def get(self, request, name, format=None):
        res = []
        for image in self.get_object(name):
            serializer = ImageProductSerializer(image)
            res.append(serializer.data)
        return Response(res)


class KeywordList(APIView):
    def get_object(self):
        try:
            return ImageProductMeta.objects.all()
        except ImageProductMeta.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        print('test')   
        res = []
        for keyword in self.get_object():
            serializer = ImageProductMetaSerializer(keyword)
            res.append(serializer.data)
        return Response(res)
