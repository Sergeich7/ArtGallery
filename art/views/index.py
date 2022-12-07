
from django.views.generic import ListView
from django.db.models import Q

from art.models import Product, Category, Technique, Author


class IndexView(ListView):
    template_name = 'art/index.html'
    context_object_name = 'all_products'
    paginate_by = 9
    page_title = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

    def get_queryset(self):
        self.page_title = ''
        slug = self.kwargs.get('slug', None)
        if slug and slug not in 'all':
            # выбираем все продукты по фильтру
            # и таблицу для определения названия категории
            mod, q = {
                'cat': [Category, Q(category__slug=slug)],
                'tec': [Technique, Q(technique__slug=slug)],
                'aut': [Author, Q(author__slug=slug)],
            }.get(self.kwargs.get('filter', None), Q())
            self.page_title = mod.objects.get(slug=slug).__str__
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

        return Product.objects.filter(q).only(
            'order', 'title', 'slug', 'created', 'description', 'thumb_of_day',
            ).order_by('order', '-created')
