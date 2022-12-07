"""Собираем общий контекст для всех страниц."""

# Задаем раз в сутки порядок сортировки и сбрасываем тумбы.
# Чтобы с кроном пока не морочиться.

import random
import datetime

from django.core.cache import cache
from django.db.models import Count, F, Value
from django.db.models.functions import Concat

from .forms import SearchForm
from .models import Product, Category, Technique, Author


def categories4menu(request):
    """Добавляем контекст - меню, количество, категории итд."""
    # сортируем выдачу работ по порядку заданному полем order
    # order задаем рандомно на 24 часа, потом снова сортируем
    if not cache.get('seed'):
        # если в кэше нет seed
        # (прошли сутки или перегружался сайт или еще что-то случилось)
        # сохраняем seed в кэш
        seed = datetime.date.today().strftime('%Y%m%d')
        cache.set('seed', seed, 60*60*24)
        # задаем новый порядок сортировки и новые тумбы если есть
        # на следующие сутки
        random.seed(int(seed))
        prod = Product.objects.all().only('order', 'thumb_of_day')
        for p in prod:
            p.order = random.randint(1, 10000)
            p.thumb_of_day = p.thumbnail
        Product.objects.bulk_update(prod, fields=['order', 'thumb_of_day'])

    context = {}

    context['query'] = request.GET.get('query', '')
    context['searchform'] = SearchForm(initial={'query': context['query']})

    context['total_obj'] = Product.objects.count()
    context['total_cat'] = Category.objects.count()
    context['total_tec'] = Technique.objects.count()
    context['total_aut'] = Author.objects.count()

    context['all_items_cat'] = Category.objects.all().\
        annotate(num_arts=Count('category_products')).order_by('title')
    context['all_items_tec'] = Technique.objects.all().\
        annotate(num_arts=Count('technique_products')).order_by('title')
    context['all_items_aut'] = Author.objects.all().\
        annotate(num_arts=Count('author_products')).\
        annotate(title=Concat(F('first_name'), Value(' '), F('last_name'))).\
        only('id', 'last_name', 'first_name', 'slug',).order_by('title')

    return context
