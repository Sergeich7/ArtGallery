"""Собираем общий контекст для всех страниц."""

from .forms import SearchForm


def categories4menu(request):
    """Добавляем контекст - меню, количество, категории итд."""
    ctx = {}

    query = ''
    if 'query' in request.GET:
        query = request.GET['query']
        ctx['query'] = query

    ctx['searchform'] = SearchForm(initial={'query': query})
    return ctx
