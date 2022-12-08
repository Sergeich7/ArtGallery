
import json
from http import HTTPStatus

from rest_framework.test import APITestCase

from art.models import Category, Author, Technique, Product


class APITests(APITestCase):

    def test_rest_api_root(self):
        resp = self.client.get(f'/api/', format='json', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertNotEqual(len(json.loads(resp.content)), 0)

    def test_rest_abs_tmp(self):
        a = Author.objects.create(
            last_name='just Author', first_name='just Author', slug='just2aut')
        c = Category.objects.create(title='just Category', slug='just2cat')
        t = Technique.objects.create(title='just Technique', slug='just2tec')
        p = Product.objects.create(
            title='just Product', slug='just2product', author=a, category=c,
            technique=t)

        resp = self.client.get(
            f'/api/list/author={p.author_id}/category={p.category_id}/technique={p.technique_id}/',
            format='json', follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)
        self.assertEqual(json.loads(resp.content).get('results')[0], {'id': p.id})

