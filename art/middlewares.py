"""Собираем общий контекст для всех страниц."""

from django.db.models import Count, F, Value
from django.db.models.functions import Concat

from .forms import SearchForm
from .models import Product, Category, Technique, Author


def categories4menu(request):
    """Добавляем контекст - меню, количество, категории итд."""
    context = {}

    context['query'] = request.GET.get('query', '')
    context['searchform'] = SearchForm(initial={'query': context['query']})

    context['total_obj'] = Product.objects.count()
    context['total_cat'] = Category.objects.count()
    context['total_tec'] = Technique.objects.count()
    context['total_aut'] = Author.objects.count()

    context['all_items_cat'] = Category.objects.all().\
        annotate(num_arts=Count('product')).order_by('title')
    context['all_items_tec'] = Technique.objects.all().\
        annotate(num_arts=Count('product')).order_by('title')
    context['all_items_aut'] = Author.objects.all().\
        annotate(num_arts=Count('product')).annotate(
            title=Concat(F('first_name'), Value(' '), F('last_name'))
            ).order_by('title')

    return context
