# Generated by Django 4.1.1 on 2022-10-05 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_remove_product_thumbnail_gallery_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
    ]
