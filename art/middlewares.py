"""Собираем общий контекст для всех страниц."""

from django.db.models import Count

from .models import Product, Category, Technique, Author
from .forms import SearchForm


def categories4menu(request):
    """Добавляем контекст - меню, количество, категории итд."""
    ctx = {}

    # узнаем сколько объектов в каждой категории b и технике 
    ctx['all_categories'] = Category.objects.all().\
        annotate(num_arts=Count('product')).order_by('title')
    ctx['all_techniques'] = Technique.objects.all().\
        annotate(num_arts=Count('product')).order_by('title')
    
    # узнаем количество
    ctx['count_obj'] = Product.objects.all().\
        aggregate(Count('id'))['id__count']
    ctx['count_cat'] = Category.objects.all().\
        aggregate(Count('id'))['id__count']
    ctx['count_tec'] = Technique.objects.all().\
        aggregate(Count('id'))['id__count']
    ctx['count_aut'] = Author.objects.all().\
        aggregate(Count('id'))['id__count']

    query = ''
    if 'query' in request.GET:
        query = request.GET['query']
        ctx['query'] = query

    ctx['searchform'] = SearchForm(initial={'query': query})
    return ctx
