# Generated by Django 3.1.5 on 2021-01-20 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytig', '0003_produitdisponible'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProduitEnPromotion',
            new_name='ProductAvailable',
        ),
        migrations.RenameModel(
            old_name='ProduitDisponible',
            new_name='ProductOnSale',
        ),
    ]
