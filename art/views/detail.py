import json

import stripe

from django.http import Http404
from django.views.generic import CreateView
from django.urls import reverse
from django import forms
from django.http import HttpResponse, HttpResponseRedirect

from art.models import Gallery, Video, Product, ArtComment

from project.settings import STRIPE_SK, STRIPE_PK



class CommentForm(forms.ModelForm):

    class Meta:
        model = ArtComment
        fields = ('text',)          # отображать только поле для ввода текста
        labels = {'text': '', }     # не отображать для него заголовок
        widgets = {
            "text": forms.Textarea(attrs={
                'cols': '30', 'rows': '5',
                'class': 'rounded-0 w-100 custom-textarea input-area', }),
        }


def create_stripe_session(request, pk_list):
    """Создает и возвращает stripe сессию для товаров из списка."""
    li = []
    products = Product.objects.all().filter(pk__in=pk_list)
    for prod in products:
        li.append({
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': f"{prod.title}",
                    'description': prod.description,
                },
                'unit_amount': 10000,
            },
            'quantity': 1,
        })
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
    session = create_stripe_session(request, [pk])
    return HttpResponse(json.dumps(session))


class DetailProdView(CreateView):
    model = ArtComment
    template_name = 'art/detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prod = Product.objects.filter(slug=self.kwargs.get('slug')).\
            select_related('author', 'category', 'technique').\
            only(
                'id', 'title', 'created', 'description',
                'materials', 'size',
                'author_id', 'category_id', 'technique_id',

                'author__id', 'author__last_name', 'author__first_name',
                'author__patronymic',

                'category__id', 'category__title',
                'technique__id', 'technique__title',
            ).first()
        if not prod:
            raise Http404
        context['product'] = prod
        context['thumbs_wo_1st'] = Gallery.objects.filter(product=prod).\
            exclude(picture=prod.thumbnail)
        context['vids'] = Video.objects.filter(product=prod)
        context['all_comments'] = ArtComment.objects.filter(product=prod)
        context['STRIPE_PK'] = STRIPE_PK
        return context


    def get_success_url(self):
        """Возврат на ту-же страницу после добавления комментария."""
        args = (self.kwargs.get('slug'),)
        return reverse('art:detail', args=args) + \
            '#comments'

    def form_valid(self, form):
        """Добавляем пользователя (комментатора) в форму."""
        form.instance.user = self.request.user
        form.instance.product =\
            Product.objects.get(slug=self.kwargs.get('slug'))
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        """Удаляем комментарий на текущей странице если нужно."""
        if kwargs.get("dc"):
            # удаляем комментарий
            cm = ArtComment.objects.filter(id=kwargs.get("dc"))
            cm.delete()
        return super().get(request, *args, **kwargs)
