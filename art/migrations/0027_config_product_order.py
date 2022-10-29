# Generated by Django 4.1.1 on 2022-10-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0026_alter_gallery_picture_alter_video_clip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Параметр')),
                ('data', models.CharField(max_length=100, verbose_name='Значение')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Позиция'),
        ),
    ]