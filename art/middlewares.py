from django.db.models import Count

from .models import Product, Category, Technique
from .forms import SearchForm


def categories4menu(request):
    """Добавляем контекст - меню, количество, категории итд."""
    # узнаем сколько объектов в каждой категории
    ctx = {}
    ctx['all_categories'] = Category.objects.all().\
        annotate(num_arts=Count('product')).order_by('title')
    ctx['all_techniques'] = Technique.objects.all().\
        annotate(num_arts=Count('product')).order_by('title')
    # узнаем сколько всего объектов
    ctx['count_obj'] = Product.objects.all().\
        aggregate(Count('id'))['id__count']
    query = ''
    if 'query' in request.GET:
        query = request.GET['query']
        ctx['query'] = query
    ctx['s_form'] = SearchForm(initial={'query': query})
    return ctx
