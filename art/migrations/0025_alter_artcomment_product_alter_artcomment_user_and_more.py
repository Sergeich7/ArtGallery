# Generated by Django 4.1.1 on 2022-10-26 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art', '0024_author_contacts_off'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artcomment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='art.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='artcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Комментатор'),
        ),
        migrations.AlterField(
            model_name='author',
            name='contacts_off',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Не показывать в форме контактов'),
        ),
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Django user'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='art.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='art.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='art.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='technique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='art.technique', verbose_name='Техника'),
        ),
        migrations.AlterField(
            model_name='video',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos', to='art.product'),
        ),
    ]