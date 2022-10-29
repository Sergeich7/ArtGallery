
from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy

from .models import Product, Category, Technique, Author


class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['art:index', 'art:contacts']

    def location(self, item):
        return reverse_lazy(item)


class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Product.objects.all().order_by('order')


class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Category.objects.all()


class TechniqueSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Technique.objects.all()


class AuthorSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Author.objects.all()


ArtSiteMaps = {
    'product': ProductSitemap,
    'category': CategorySitemap,
    'technique': TechniqueSitemap,
    'author': AuthorSitemap,
    'static': StaticSitemap
    }
