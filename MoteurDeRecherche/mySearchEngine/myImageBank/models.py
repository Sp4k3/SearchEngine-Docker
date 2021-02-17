from django.db import models

# Create your models here.
class ImageProduct(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url = models.TextField(default='default')
    metadata = models.TextField(default=[])

    class Meta:
        ordering = ('url',)

class ImageProductMeta(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    keyword = models.TextField(default='default')
    idList = models.TextField(default='default')

    class Meta:
        ordering = ('keyword',)