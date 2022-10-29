# Generated by Django 4.1.1 on 2022-10-29 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0028_alter_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='th_of_day',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pic', to='art.gallery', verbose_name='Тумба дня'),
        ),
    ]
