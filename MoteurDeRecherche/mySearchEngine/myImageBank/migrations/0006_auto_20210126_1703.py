# Generated by Django 3.1.5 on 2021-01-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myImageBank', '0005_auto_20210126_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageproductmeta',
            name='idList',
            field=models.TextField(default='default'),
        ),
    ]