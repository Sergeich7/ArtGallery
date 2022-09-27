import random
from datetime import date

from django.views.generic import ListView
from django.db.models import Q
from django.db.models import CharField, TextField
from django.db.models.functions import Lower

from art.views import AddContextMixin
from art.models import Product


class IndexView(AddContextMixin, ListView):
    template_name = 'art/index.html'
    context_object_name = 'all_products'
    paginate_by = 8


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.add_context(context, active_cat=self.active_cat)

    def get_queryset(self):
        # отображаем все продукты
        q = Q()
        self.active_cat = '0cat'
        if self.kwargs.get('pk'):
            pk = self.kwargs.get('pk')
            self.active_cat = f'{pk}{self.kwargs.get("filter")}'
            if pk not in '0':
                if 'cat' in self.kwargs.get('filter'):
                    # отображаем продукты только определенной категории
                    q = Q(category=pk)
                else:
                    # отображаем продукты только определенной техники
                    q = Q(technique=pk)
        else:
            if 'query' in self.request.GET:
                query = self.request.GET['query']
                if len(query):
                    # ищем
                    self.active_cat = 'active_cat'
#                    q = Q(title__iexact=query) |\
#                        Q(description__iexact=query) |\
#                        Q(materials__iexact=query) |\
#                        Q(category__title__iexact=query) |\
#                        Q(author__last_name__iexact=query) |\
#                        Q(technique__title__iexact=query)
                    CharField.register_lookup(Lower, "lower")
                    TextField.register_lookup(Lower, "lower")
                    q = Q(title__lower__icontains=query) |\
                        Q(description__lower__icontains=query) |\
                        Q(materials__lower__icontains=query) |\
                        Q(category__title__lower__icontains=query) |\
                        Q(author__last_name__lower__icontains=query) |\
                        Q(technique__title__lower__icontains=query)
        not_sorted_qs = Product.objects.filter(q)
        # сортирую вывод каждый день по разному,
        # пусть хоть что-то иногда меняется на сайте
        # annotation не получилось, почему-то всегда аннотируется
        # одним и тем-же значением. random вызывается только 1 раз
        sort_by = (
            'id', '-id', 'description', '-description',
            'thumbnail', '-thumbnail',
            )
        random.seed(int(str(date.today()).replace('-', '')))
        return not_sorted_qs.order_by(
            sort_by[random.randint(0, len(sort_by)-1)])
