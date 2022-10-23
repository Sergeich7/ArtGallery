"""Тестируем модель и все что с ней связано, чтобы не создавать\
            базу по несколько раз."""
            
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from art.models import Category, Author, Technique, Product, ArtComment


class DetailViewTest(TestCase):

    def setUp(self):
        """Создаем тестовую модель."""
        a = Author.objects.create(
            last_name='just Author', first_name='just Author', slug='just1aut')
        c = Category.objects.create(title='just Category', slug='just1cat')
        t = Technique.objects.create(title='just Technique', slug='just1tec')
        p = Product.objects.create(
            title='just Product', slug='just1product', author=a, category=c,
            technique=t)
        p.images.create(picture="picname.jpg")
        u = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )
        ArtComment.objects.create(text='just ArtComment', product=p, user=u)

    def test_art_model(self):
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

    def test_detail_abs_tmp(self):
        resp = self.client.get('/just1product/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/detail.html')

    def test_detail_rev(self):
        resp = self.client.get(
            reverse('art:detail', args=['just1product']), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_cat_abs_tmp(self):
        resp = self.client.get('/cat/just1cat/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/index.html')

    def test_cat_rev(self):
        resp = self.client.get(
            reverse('art:filter', args=['cat', 'just1cat']), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_tec_abs_tmp(self):
        resp = self.client.get('/tec/just1tec/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/index.html')

    def test_tec_rev(self):
        resp = self.client.get(
            reverse('art:filter', args=['tec', 'just1tec']), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_aut_abs_tmp(self):
        resp = self.client.get('/aut/just1aut/', follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'art/index.html')

    def test_aut_rev(self):
        resp = self.client.get(
            reverse('art:filter', args=['aut', 'just1aut']), follow=True)
        self.assertEqual(resp.status_code, 200)

