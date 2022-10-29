
from multiprocessing import get_context
from django.views.generic import ListView
from django.db.models import Q

from art.models import Product


class IndexView(ListView):
    template_name = 'art/index.html'
    context_object_name = 'all_products'
    paginate_by = 9

    def get_queryset(self):
        slug = self.kwargs.get('slug', None)
        if slug and slug not in 'all':
            # выбираем все продукты по фильтру
            q = {
                'cat': Q(category__slug=slug),
                'tec': Q(technique__slug=slug),
                'aut': Q(author__slug=slug),
            }.get(self.kwargs.get('filter', None), Q())
        else:
            query = self.request.GET.get('query', None)
            if query:
                # запрос в модель на поиск
                # в SQLite не работает регистронезависимый поиск
                # в MySQL все работает норм
                q = Q(title__icontains=query) |\
                    Q(description__icontains=query) |\
                    Q(materials__icontains=query) |\
                    Q(category__title__icontains=query) |\
                    Q(author__last_name__icontains=query) |\
                    Q(technique__title__icontains=query)
            else:
                # выбираем все продукты
                q = Q()
        prods = Product.objects.filter(q).select_related('th_of_day').\
            order_by('order', '-created')
        return prods
