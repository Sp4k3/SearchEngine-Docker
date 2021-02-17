from django.core.management.base import BaseCommand, CommandError
from myImageBank.models import ImageProduct
from myImageBank.serializers import ImageProductSerializer
from myImageBank.config import randomImageUrl
import requests
import time


class Command(BaseCommand):
    help = 'Refresh the list of image URL.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        ImageProduct.objects.all().delete()
        for image in randomImageUrl:
            meta = image.split('/')[-1].split('_')[0].split('-')
            formatedMeta = ','.join(str(x) for x in meta)
            serializer = ImageProductSerializer(
                data={ 'url': str(image), 'metadata': formatedMeta }
            )
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(
                    '[' + time.ctime() + '] Successfully added product URL="%s"' % image
                ))

        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')

