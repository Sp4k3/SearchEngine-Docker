from django.core.management.base import BaseCommand, CommandError
from myImageBank.models import ImageProduct
from myImageBank.models import ImageProductMeta
from myImageBank.serializers import ImageProductSerializer
from myImageBank.serializers import ImageProductMetaSerializer
from myImageBank.config import randomImageUrl
import requests
import time


class Command(BaseCommand):
    help = 'Refresh the list of image URL.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        ImageProductMeta.objects.all().delete()

        images = ImageProduct.objects.all()
        keywords = []
        temp = []
        for image in images:
            serializer = ImageProductSerializer(image)
            meta = [serializer.data['metadata'].split(','), serializer.data['id']]
            for metadata in meta[0]:
                if metadata not in temp:
                    keywords.append({ 'keyword': metadata, 'idList': [meta[1]] })
                    temp.append(metadata)
                else:
                    for keyword in keywords:
                        if keyword['keyword'] == metadata:
                            keyword['idList'].append(meta[1])
                            
        for keyword in keywords:
            formatedIdList = ','.join(str(x) for x in keyword['idList'])
            serializer = ImageProductMetaSerializer(
                data={ 'keyword': str(keyword['keyword']), 'idList': formatedIdList }
            )
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(
                    '[' + time.ctime() + '] Successfully added product URL="%s"' % image
                ))

        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')

