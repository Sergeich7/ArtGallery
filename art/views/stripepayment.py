import json

import stripe

from django.urls import reverse
from django.http import HttpResponse

from art.models import Product

from project.settings import STRIPE_SK

from .favorites import Cart


def create_stripe_session(request, pk_list):
    """Создает и возвращает stripe сессию для товаров из списка."""

    products = Product.objects.all().filter(pk__in=pk_list)

    li = [{
        'price_data': {
            'currency': 'rub',
            'product_data': {
                'name': prod.title,
                'description': prod.description,
            },
            'unit_amount': int(prod.price*100),
        },
        'quantity': 1,
    } for prod in products if prod.price > 0]

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
    return stripe.checkout.Session.create(**sp)


def session_to_json(request, pk):
    """Упаковываем и отдаем сессию в json формате."""
    # если передали pk, то один продукт покупаем.
    # иначе  берем из сессий

    pk_list = [pk] if int(pk) > 0 else Cart(request).cart.keys()
    print(pk_list)
    session = create_stripe_session(request, pk_list)
    return HttpResponse(json.dumps(session))


