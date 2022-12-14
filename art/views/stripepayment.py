import stripe

from django.urls import reverse
from django.views import View
from django.http import JsonResponse

from project.settings import STRIPE_SK

from art.models import Product
from .favorites import Cart


class StripeBuyView(View):

    def get(self, request, **kwargs):
        """Упаковываем и отдаем сессию в json формате."""
        # если передали pk > 0, то один продукт покупаем.
        # иначе  берем из сессий
        pk = self.kwargs.get('pk', '0')
        pk_list = [pk] if int(pk) > 0 else Cart(request).cart.keys()
        products = Product.objects.all().filter(pk__in=pk_list)

        # Добавляем к покупке только товары с ценой
        li = [{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': product.title,
                    'description': product.description,
                },
                'unit_amount': int(product.price*100),
            },
            'quantity': 1,
        } for product in products if product.price > 0]

        if li:
            # если есть хоть 1 товар к покупке, создаем сессию
            sp = dict(
                submit_type='donate',
                billing_address_collection='auto',
                line_items=li,
                mode='payment',
                locale='ru',
                success_url=request.build_absolute_uri(reverse('art:payment_success')),
                cancel_url=request.build_absolute_uri(reverse('art:payment_cancel')),
            )
            stripe.api_key = STRIPE_SK
            return JsonResponse(stripe.checkout.Session.create(**sp))

        return JsonResponse({'error': 'No sales items'})


