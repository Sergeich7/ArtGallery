import random

from django import template
from django.db.models import Count, F, Value
from django.db.models.functions import Concat

from ..models import Product, Category, Technique, Author

register = template.Library()

@register.inclusion_tag('menu_items_cat_tec.html')
def menu_items_cat_tec(items_type='cat', fl_no_all='all'):
    # узнаем сколько объектов в каждой категории или технике 
    if items_type == 'cat':
        all_items = Category.objects.all().\
            annotate(num_arts=Count('product')).order_by('title')
    elif items_type == 'tec':
        all_items = Technique.objects.all().\
            annotate(num_arts=Count('product')).order_by('title')
    elif items_type == 'aut':
        all_items = Author.objects.all().\
            annotate(num_arts=Count('product')).annotate(
                title=Concat(F('first_name'), Value(' '), F('last_name'))
                ).order_by('title')
    return {
        'all_items': all_items, 
        'items_type': items_type, 
        'items_no_all': fl_no_all
    }

@register.simple_tag
def total_obj():
    return Product.objects.count()

@register.simple_tag(name='total_cat')
def total_cat():
    return Category.objects.count()

@register.simple_tag
def total_tec():
    return Technique.objects.count()

@register.simple_tag
def total_aut():
    return Author.objects.count()

@register.simple_tag
def random_int(a, b=None):
    if b is None:
        b = a
    return random.randint(a, b)
