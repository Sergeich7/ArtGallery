import random
from datetime import date

from django.views.generic import ListView
from django.db.models import Value, FloatField

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
        not_sorted_qs = Product.objects.all()
        self.active_cat = self.kwargs.get('pk', 0)
        if self.kwargs.get('pk'):
            # отображаем продукты только определенной категории
            not_sorted_qs = Product.objects.filter(
                category=self.kwargs.get('pk'))
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
