from django.db import models


class ProductOnSale(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')
    class Meta:
        ordering = ('tigID',)


class ProductAvailable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tigID = models.IntegerField(default='-1')
    class Meta:
        ordering = ('tigID',)