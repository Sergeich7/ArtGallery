from decimal import Decimal

from django.conf import settings
from django.views.generic.base import RedirectView
from django.urls import reverse
from art.models import Product


class Cart():
    """Класс для работы с избранным в сессии."""

    def __init__(self, request):
        """Инициализация избранных."""
        self.session = request.session
        cart = self.session.get(settings.FAVORITES_SESSION_ID)
        if not cart:
            # Сохраняем пустую сессию
            cart = self.session[settings.FAVORITES_SESSION_ID] = {}
        self.cart = cart

    def add(self, product):
        """Добавление товара в корзину."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price)}
            self.save()

    def save(self):
        """Помечаем сессию как измененную"""
        self.session.modified = True

    def remove(self, product):
        """Удаление товара из корзины."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __len__(self):
        return len(self.cart.values())

#    def __iter__(self):
#        product_ids = self.cart.keys()
#        products = Product.objects.filter(id__in=product_ids)
#        cart = self.cart.copy()
#        for product in products:
#            cart[str(product.id)]['product'] = product
#        for item in cart.values():
#            item['price'] = Decimal(item['price'])
#        yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.FAVORITES_SESSION_ID]
        self.save()


class FavoritesCMD(RedirectView):
    """Управление избранными."""

    def get_redirect_url(self, *args, **kwargs):
        """Управление избранными."""
        # по умолчанию редиректим на ту-же страницу, откуда пришел запрос
        self.url = self.request.META.get('HTTP_REFERER')
        cart = Cart(self.request)
        if kwargs['pk']:
            product = Product.objects.get(pk=kwargs.get('pk'))
            if kwargs['cmd'] == 'add':
                # добавляем продукт в избранные
                cart.add(product)
            elif kwargs['cmd'] == 'remove':
                # удаляем продукт из избранных
                cart.remove(product)
        elif kwargs['cmd'] == 'clear':
            # очищаем корзину и редиректим на index
            cart.clear()
            self.url = reverse('art:index')

        return super().get_redirect_url(*args, **kwargs)
