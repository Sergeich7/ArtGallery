
from django import template
from django.db.models import Count

from ..models import Product, Category, Technique, Author

register = template.Library()

@register.inclusion_tag('menu_items_cat_tec.html')
def menu_items_cat_tec(items_type='cat'):
    # узнаем сколько объектов в каждой категории или технике 
    if items_type == 'cat':
        all_items = Category.objects.all().\
            annotate(num_arts=Count('product')).order_by('title')
    else:
        all_items = Technique.objects.all().\
            annotate(num_arts=Count('product')).order_by('title')
    return {'all_items': all_items, 'items_type': items_type}

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

