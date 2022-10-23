"""Определяем свои тэги."""

import random

from django import template


register = template.Library()


@register.inclusion_tag('menu_items_cat_tec.html', takes_context=True)
def menu_items_cat_tec(context, items_type='cat', fl_no_all='all'):
    """Тэг генерит html меню (категории, техники, авторы)."""
    # тег вызывается 9 раз для одной страницы, те обращение к базе
    # не желательно.
    # если fl_no_all='all', то добавляет строку с общим количеством работ.
    return {
        'items_type': items_type,
        'items_no_all': fl_no_all,
        'total_obj': context['total_obj'],
        'all_items': context[f'all_items_{items_type}'],
    }


@register.simple_tag
def random_int(a, b=None):
    """Тэг с номером текущего желтого фона. Выбирается ранодомно."""
    if b is None:
        b = a
    return random.randint(a, b)
