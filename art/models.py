#from pyexpat import model
from enum import unique
import cv2
import moviepy.editor as mp

from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    """Сделал на будущее. Может будет несколько авторов на сайте."""

    last_name = models.CharField(
        max_length=30, blank=False, verbose_name='Фамилия',)
    first_name = models.CharField(max_length=30, verbose_name='Имя',)
    patronymic = models.CharField(max_length=30, verbose_name='Отчество',)
#    slug = models.SlugField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    email = models.EmailField(max_length=50)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='Django user',)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'.strip()

    class Meta:
        """Что-бы в админке красиво было."""

        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['last_name']


class Category(models.Model):
    title = models.CharField(
        max_length=30, verbose_name='Категория')
#    slug = models.SlugField(max_length=30, null=True, blank=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        """Что-бы в админке красиво было."""

        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['title']


class Technique(models.Model):
    title = models.CharField(
        max_length=30, verbose_name='Техника')
#    slug = models.SlugField(max_length=30, null=True, blank=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        """Что-бы в админке красиво было."""

        verbose_name = 'Техника'
        verbose_name_plural = 'Техники'
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
#    slug = models.SlugField(max_length=100, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateField(null=True, verbose_name='Дата создания')
    description = models.TextField(verbose_name='Описание')
    materials = models.CharField(
        max_length=200, verbose_name='Материалы')
    size = models.CharField(max_length=20, blank=True, verbose_name='Размер')

    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория')
    technique = models.ForeignKey(
        Technique, on_delete=models.CASCADE, verbose_name='Техника')


    def __str__(self):
        return self.title

    class Meta:
        """Что-бы в админке красиво было."""

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
        verbose_name='Продукт')

    def __str__(self):
        return str(self.text)

    class Meta:
        """Что-бы в админке красиво было."""

        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-published']


class Gallery(models.Model):
    picture = models.ImageField(
        upload_to='gallery', verbose_name='Фотографии')
    vertical = models.BooleanField(default=False, editable=False)
    thumb = models.BooleanField(default=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        """Что-бы в админке красиво было."""

        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def save(self, *args, **kwargs):
        """Проверка картинки на вертикальность."""
        """Чтобы не проверять каждый раз при отображении"""
        super().save(*args, **kwargs)
        # if self.picture.height > self.picture.width:
        #   self.vertical = True
        # иногда у картинки перепутаны размер. скорее всего в файле что-то.
        # битый может битый, а может в PIL какой косяк
        # получаю размеры при помощи OpenCV
        height, width, _ = cv2.imread(self.picture.path).shape
        if height > width:
            self.vertical = True
            super().save(*args, **kwargs)


class Video(models.Model):
    clip = models.FileField(
        upload_to='videos', blank=True, verbose_name='Видео')
    vertical = models.BooleanField(default=False, editable=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='videos')

    def save(self, *args, **kwargs):
        """Проверка видео на вертикальность."""
        """Чтобы не проверять каждый раз при отображении"""
        super().save(*args, **kwargs)
        if self.clip:
            clip1 = mp.VideoFileClip(self.clip.path)
            if clip1.h < clip1.w:
                self.vertical = True
        super().save(*args, **kwargs)

    class Meta:
        """Что-бы в админке красиво было."""

        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

