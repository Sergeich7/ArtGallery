# Generated by Django 4.1.1 on 2022-10-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0009_author_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
