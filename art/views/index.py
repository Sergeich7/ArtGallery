import random

from django.views.generic import ListView
from django.db.models import Q, Count
from django.db.models import CharField, TextField, Subquery, OuterRef, ImageField, ExpressionWrapper, Exists
from django.db.models.functions import Lower

from art.models import Gallery, Product, Category, Technique


class IndexView(ListView):
    template_name = 'art/index.html'
    context_object_name = 'all_products'
    page_title = ''
    paginate_by = 9


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

    def get_queryset(self):
        # отображаем все продукты
        q = Q()
        if self.kwargs.get('filter'):
        # фильтр по категории или техники
            if 'cat' in self.kwargs.get('filter'):
                # отображаем продукты только определенной категории
                if self.kwargs.get('pk'):
                    # выводим категории по id
                    pk = self.kwargs.get('pk')
                    if pk not in '0':
                        q = Q(category=pk)
                        self.page_title = Category.objects.get(pk=pk)
                else:
                    # выводим категории по slug
                    slug = self.kwargs.get('slug')
                    if slug not in 'all':
                        q = Q(category__slug=slug)
                        self.page_title = Category.objects.get(slug=slug)
            else:
                # отображаем продукты только определенной техники
                if self.kwargs.get('pk'):
                    # выводим техники по id
                    pk = self.kwargs.get('pk')
                    q = Q(technique=pk)
                    self.page_title = Technique.objects.get(pk=pk)
                else:
                    # выводим техники по slug
                    slug = self.kwargs.get('slug')
                    if slug not in 'all':
                        q = Q(technique__slug=slug)
                        self.page_title = Technique.objects.get(slug=slug)
        else:
            if 'query' in self.request.GET:
                # Поиск
                query = self.request.GET['query']
                if len(query):
                    # ищем
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

        # has_thumb=True если есть выбранные хорошие картинки
        sq_has_thumb = Exists(
            # True - Есть картинки выбранные под тумбы
            Gallery.objects.filter(product=OuterRef('pk')).filter(thumb=True)
        )
        not_sorted_qs = not_sorted_qs.annotate(has_thumb=sq_has_thumb)

        # выбираем картинку под тумбу для тех,
        # где нет выбранных под тумбы рандомно из всех
        sq = Subquery(
            # Рандомная тумба из всех тумб
            Gallery.objects.filter(product=OuterRef('pk')).\
                order_by('?')[:1].values('picture')
        )
        p1 = not_sorted_qs.annotate(th=sq).filter(has_thumb=False)

        # выбираем картинку под тумбу для тех,
        # где есть выбранные под тумбы рандомно из всех выбранных
        sq = Subquery(
            # Рандомная тумба из выбранных тумб
            Gallery.objects.filter(product=OuterRef('pk')).filter(thumb=True).\
                order_by('?')[:1].values('picture')
        )
        p2 = not_sorted_qs.annotate(th=sq).filter(has_thumb=True)

        not_sorted_qs = p1.union(p2)

        return not_sorted_qs.order_by('-created')
        
