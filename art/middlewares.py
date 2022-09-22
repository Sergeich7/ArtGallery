from django.db.models import Count

from .models import Product, Category


def categories4menu(request):
    """Добавляем контекст - меню, количество, категории итд."""
    # узнаем сколько объектов в каждой категории
    ctx = {}
    ctx['all_categories'] = Category.objects.all().\
        annotate(num_arts=Count('product')).order_by('title')
    # узнаем сколько всего объектов
    ctx['count_obj'] = Product.objects.all().\
        aggregate(Count('id'))['id__count']
    return ctx
