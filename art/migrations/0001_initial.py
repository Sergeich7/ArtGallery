# Generated by Django 4.1.3 on 2022-12-08 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('contacts_off', models.BooleanField(blank=True, default=False, null=True, verbose_name='Не показывать в форме контактов')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Django user')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Параметр')),
                ('data', models.CharField(max_length=100, verbose_name='Значение')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Позиция')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('created', models.DateField(null=True, verbose_name='Дата создания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('materials', models.CharField(max_length=200, verbose_name='Материалы')),
                ('size', models.CharField(blank=True, max_length=20, verbose_name='Размер')),
                ('thumb_of_day', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Тумба дня')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_products', to='art.author', verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_products', to='art.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Техника')),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Техника',
                'verbose_name_plural': 'Техники',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clip', models.FileField(blank=True, upload_to='videos/%Y/%m/%d/', verbose_name='Видео')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='art.product')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='technique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technique_products', to='art.technique', verbose_name='Техника'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='gallery/%Y/%m/%d/', verbose_name='Фотографии')),
                ('thumb', models.BooleanField(default=False, verbose_name='Хорошая')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='art.product')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='ArtComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art.product', verbose_name='Продукт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Комментатор')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-published'],
            },
        ),
    ]
