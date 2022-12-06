import random

from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    """Авторы."""

    last_name = models.CharField(
        max_length=30, blank=False, verbose_name='Фамилия',)
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')

    slug = models.SlugField(max_length=100, unique=True, db_index=True,)

    email = models.EmailField(max_length=50,)
    # не отображать email в форме обратной связи
    contacts_off = models.BooleanField(
        default=False, blank=True, null=True,
        verbose_name='Не показывать в форме контактов')
    # ассоциированные пользователь (может и не быть)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='Django user',)

    def get_absolute_url(self):
        return reverse(
            'art:filter',
            kwargs={'filter': 'aut', 'slug': self.slug})

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'.strip()

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name', 'first_name']


class Category(models.Model):
    title = models.CharField(
        max_length=30, verbose_name='Категория')
    slug = models.SlugField(max_length=30, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse(
            'art:filter', kwargs={'filter': 'cat', 'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['title']


class Technique(models.Model):
    title = models.CharField(
        max_length=30, verbose_name='Техника')
    slug = models.SlugField(max_length=30, unique=True)

    def get_absolute_url(self):
        return reverse(
            'art:filter', kwargs={'filter': 'tec', 'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техники'
        ordering = ['title']


class Product(models.Model):
    order = models.IntegerField(
        blank=True, null=True, db_index=True, verbose_name='Позиция')
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    created = models.DateField(null=True, verbose_name='Дата создания')
    description = models.TextField(verbose_name='Описание')
    materials = models.CharField(
        max_length=200, verbose_name='Материалы')
    size = models.CharField(max_length=20, blank=True, verbose_name='Размер')

    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author_products',
        verbose_name='Автор')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_products',
        verbose_name='Категория')
    technique = models.ForeignKey(
        Technique, on_delete=models.CASCADE, related_name='technique_products',
        verbose_name='Техника')

    thumb_of_day = models.ImageField(
        null=True, blank=True, verbose_name='Тумба дня')

    @property
    def thumbnail(self):
        """Возвращает тумбу дня. Если не тумба определена, \
            то вычисляет и сохраняет)."""
        if not self.thumb_of_day:
            # назначаем тумбу дня если не назначена еще
            g = Gallery.objects.filter(product=self.pk, thumb=True).\
                only('picture',).order_by('?').first()
            if not g:
                g = Gallery.objects.filter(product=self.pk).\
                    only('picture',).order_by('?').first()
            self.thumb_of_day = g.picture
            self.save(update_fields=['thumb_of_day'])
        return self.thumb_of_day

    def save(self, *args, **kwargs):
        self.order = random.randint(1, 10000)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('art:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ArtComment(models.Model):
    text = models.TextField(verbose_name='Текст', blank=False)
    published = models.DateTimeField(
        auto_now_add=True, blank=False, verbose_name='Опубликовано')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Комментатор',)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name='Продукт',)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-published']


class Gallery(models.Model):
    picture = models.ImageField(
        upload_to='gallery/%Y/%m/%d/', verbose_name='Фотографии')
    thumb = models.BooleanField(default=False, verbose_name='Хорошая')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return str(self.picture)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Video(models.Model):
    clip = models.FileField(
        upload_to='videos/%Y/%m/%d/', blank=True, verbose_name='Видео')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return str(self.clip)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Config(models.Model):
    name = models.CharField(max_length=100, verbose_name='Параметр')
    data = models.CharField(max_length=100, verbose_name='Значение')
