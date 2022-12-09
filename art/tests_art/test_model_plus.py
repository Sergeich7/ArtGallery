"""Тестируем модель и все что с ней связано, чтобы не создавать\
            базу по несколько раз."""

import json
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from art.models import Category, Author, Technique, Product, ArtComment
from .model_setup import ModelSetupMixin


class ArtModelTest(ModelSetupMixin, TestCase):

    # setUp(self): наследуем из ModelSetupMixin

    def test_model(self):
        """Тестируем модель."""
        tst_obj = Category.objects.get(slug='just1cat')
        expected_object_field = f'{tst_obj.title}'
        self.assertEqual(expected_object_field, 'just Category')

        tst_obj = Author.objects.get(slug='just1aut')
        expected_object_field = f'{tst_obj.last_name}'
        self.assertEqual(expected_object_field, 'just Author')

        tst_obj = Technique.objects.get(slug='just1tec')
        expected_object_field = f'{tst_obj.title}'
        self.assertEqual(expected_object_field, 'just Technique')
        tst_prod = Product.objects.get(slug='just1product')
        expected_object_field = f'{tst_prod.title}'
        self.assertEqual(expected_object_field, 'just Product')

        tst_obj = ArtComment.objects.get(product=tst_prod)
        expected_object_field = f'{tst_obj.text}'
        self.assertEqual(expected_object_field, 'just ArtComment')

        tst_obj = get_user_model().objects.get(username=tst_obj.user)
        expected_object_field = f'{tst_obj.email}'
        self.assertEqual(expected_object_field, 'test@email.com')

    #
    # detail
    #

    def test_detail_absoluteurl_tmplate(self):
        resp = self.client.get('/just1product/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/detail.html')

    def test_detail_get_wrong_product(self):
        resp = self.client.get('/wrong1product/', follow=True)
        self.assertEqual(resp.status_code, 404)

    def test_detail_reverseurl(self):
        resp = self.client.get(
            reverse('art:detail', args=['just1product']), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_detail_buy_stripe(self):
        """Сессия stripe для покупки продукта."""
        resp = self.client.get(f'/buy/{self.prod1.id}', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertContains(resp, 'cs_test_')

    #
    # index
    #

    def test_index_absoluteurl_tmplate(self):
        resp = self.client.get('/?query=duct', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertContains(resp, 'just Product')
        self.assertTemplateUsed(resp, 'art/index.html')

    def test_index_reverseurl(self):
        resp = self.client.get(reverse('art:index'), follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)

    #
    # params
    #

    def test_cat_absoluteurl_tmplate(self):
        resp = self.client.get('/cat/just1cat/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/index.html')

    def test_cat_reverseurl(self):
        resp = self.client.get(
            reverse('art:filter', args=['cat', 'just1cat']), follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)

    def test_tec_absoluteurl_tmplate(self):
        resp = self.client.get('/tec/just1tec/', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(resp, 'art/index.html')

    def test_tec_reverseurl(self):
        resp = self.client.get(
            reverse('art:filter', args=['tec', 'just1tec']), follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)

    def test_aut_absoluteurl_tmplate(self):
        resp = self.client.get('/aut/just1aut/', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(resp, 'art/index.html')

    def test_aut_reverseurl(self):
        resp = self.client.get(
            reverse('art:filter', args=['aut', 'just1aut']), follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)

    #
    # sitemap
    #

    def test_sitemap_absoluteurl(self):
        resp = self.client.get('/sitemap.xml', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertContains(resp, 'just1product')
